from rest_framework import generics, views
from rest_framework.response import Response
import jwt

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .. import models
from . import serializers


class ReviewTokenMixin:
    authentication_classes = []

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        review_token = self.request.META.get('HTTP_X_REVIEW_TOKEN')
        data = jwt.decode(review_token, settings.SECRET_KEY, algorithms=['HS256'])
        self.reviewer_id = data['reviewer_id']
        self.page_revision_id = data['page_revision_id']

        return super().dispatch(*args, **kwargs)


class CommentList(ReviewTokenMixin, generics.ListCreateAPIView):
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        return models.Comment.objects.filter(page_revision_id=self.page_revision_id)

    def perform_create(self, serializer):
        serializer.save(reviewer_id=self.reviewer_id, page_revision_id=self.page_revision_id)


class Comment(ReviewTokenMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CommentSerializer

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

    def get_queryset(self):
        return models.CommentReply.objects.filter(comment_id=self.kwargs['comment_pk'])
