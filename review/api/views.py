from rest_framework import generics
import jwt

from django.conf import settings
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
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def perform_create(self, serializer):
        serializer.save(reviewer_id=self.reviewer_id, page_revision_id=self.page_revision_id)


class Comment(ReviewTokenMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer


# class CommentResolved():


class CommentReplyList(ReviewTokenMixin, generics.ListCreateAPIView):
    queryset = models.CommentReply.objects.all()
    serializer_class = serializers.CommentReplySerializer


class CommentReply(ReviewTokenMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CommentReply.objects.all()
    serializer_class = serializers.CommentReplySerializer
