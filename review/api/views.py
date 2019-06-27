from datetime import timedelta

from rest_framework import generics, status, views
from rest_framework.response import Response
import jwt

from django.conf import settings
from django.db import transaction
from django.db.models import Case, F, Value, When
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .. import models
from . import serializers


class ReviewTokenMixin:
    authentication_classes = []

    def process_review_token(self, data):
        self.reviewer_id = data['reviewer_id']
        self.page_revision_id = data['page_revision_id']
        self.share_id = data.get('share_id')

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        review_token = self.request.META.get('HTTP_X_REVIEW_TOKEN')
        data = jwt.decode(review_token, settings.SECRET_KEY, algorithms=['HS256'])
        self.process_review_token(data)

        return super().dispatch(*args, **kwargs)


class CommentList(ReviewTokenMixin, generics.ListCreateAPIView):
    serializer_class = serializers.CommentSerializer

    def get(self, *args, **kwargs):
        now = timezone.now()

        if self.share_id is not None:
            models.Share.objects.filter(id=self.share_id).update(
                first_accessed_at=Case(
                    When(first_accessed_at__isnull=True, then=Value(now)),
                    default=F('first_accessed_at'),
                ),
                last_accessed_at=now,
            )

        return super().get(*args, **kwargs)

    def get_queryset(self):
        return models.Comment.objects.filter(page_revision_id=self.page_revision_id)

    def perform_create(self, serializer):
        serializer.save(reviewer_id=self.reviewer_id, page_revision_id=self.page_revision_id)


class Comment(ReviewTokenMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CommentSerializer

    def update(self, *args, **kwargs):
        comment = self.get_object()
        if comment.reviewer_id != self.reviewer_id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        return super().update(*args, **kwargs)

    def destroy(self, *args, **kwargs):
        comment = self.get_object()
        if comment.reviewer_id != self.reviewer_id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        return super().destroy(*args, **kwargs)

    def get_queryset(self):
        return models.Comment.objects.filter(page_revision_id=self.page_revision_id)


class CommentResolved(ReviewTokenMixin, views.APIView):
    def put(self, *args, **kwargs):
        comment = get_object_or_404(models.Comment.objects.filter(page_revision_id=self.page_revision_id), id=kwargs['pk'])
        comment.is_resolved = True
        comment.save(update_fields=['is_resolved'])
        return Response()

    def delete(self, *args, **kwargs):
        comment = get_object_or_404(models.Comment.objects.filter(page_revision_id=self.page_revision_id), id=kwargs['pk'])
        comment.is_resolved = False
        comment.save(update_fields=['is_resolved'])
        return Response()


class CommentReplyList(ReviewTokenMixin, generics.ListCreateAPIView):
    serializer_class = serializers.CommentReplySerializer

    def get_queryset(self):
        return models.CommentReply.objects.filter(comment_id=self.kwargs['pk']).order_by('created_at')

    def perform_create(self, serializer):
        # TODO: Make sure self.kwargs['comment_pk'] is on the current page revision
        serializer.save(reviewer_id=self.reviewer_id, comment_id=self.kwargs['pk'])


class CommentReply(ReviewTokenMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CommentReplySerializer

    def update(self, *args, **kwargs):
        reply = self.get_object()
        if reply.reviewer_id != self.reviewer_id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        return super().update(*args, **kwargs)

    def destroy(self, *args, **kwargs):
        reply = self.get_object()
        if reply.reviewer_id != self.reviewer_id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        return super().destroy(*args, **kwargs)

    def get_queryset(self):
        return models.CommentReply.objects.filter(comment_id=self.kwargs['comment_pk'])


class ModerationMixin(ReviewTokenMixin):
    def process_review_token(self, data):
        super().process_review_token(data)

        # Prevent users from using moderation APIs for review tokens that don't
        # have moderation enabled
        if not data.get('moderation_enabled', False):
            raise Http404

        self.moderation_request = get_object_or_404(models.ModerationRequest, revision_id=self.page_revision_id)


class ModerationLock(ModerationMixin, views.APIView):
    def put(self, *args, **kwargs):
        lock_extension = timedelta(minutes=settings.MODERATION_LOCK_TIMEOUT)

        # TODO: Add "locked by" field to avoid race condition
        self.moderation_request.locked_until = timezone.now() + lock_extension
        self.moderation_request.save()

        return Response()

    def delete(self, *args, **kwargs):
        self.moderation_request.locked_until = None
        self.moderation_request.save()

        return Response()


class ModerationRespond(ModerationMixin, generics.CreateAPIView):
    queryset = models.ModerationResponse.objects.all()
    serializer_class = serializers.ModerationResponseSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        serializer.save(reviewer_id=self.reviewer_id, request=self.moderation_request)
        self.moderation_request.locked_until = None
        self.moderation_request.save()
