from datetime import timedelta

from rest_framework import generics, views, status
from rest_framework.response import Response

from django.conf import settings
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from review.api.views import ReviewTokenMixin

from .. import models
from . import serializers


class ModerationMixin(ReviewTokenMixin):
    def process_review_token(self, data):
        super().process_review_token(data)

        # Prevent users from using moderation APIs for review tokens that don't
        # have moderation enabled
        if not data.get('moderation_enabled', False):
            raise Http404

        self.moderation = get_object_or_404(models.Moderation, revision_id=self.page_revision_id)


class ModerationLock(ModerationMixin, views.APIView):
    def put(self, *args, **kwargs):
        lock_extension = timedelta(minutes=settings.MODERATION_LOCK_TIMEOUT)
        new_lock_time = timezone.now() + lock_extension

        # TODO: Add "locked by" field to avoid race condition
        self.moderation.locked_until = timezone.now() + lock_extension
        self.moderation.save()

        return Response()

    def delete(self, *args, **kwargs):
        self.moderation.locked_until = None
        self.moderation.save()

        return Response()


class ModerationRespond(ModerationMixin, generics.CreateAPIView):
    queryset = models.ModeratorReview.objects.all()
    serializer_class = serializers.ModeratorReviewSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        serializer.save(moderation=self.moderation)
        self.moderation.locked_until = None
        self.moderation.save()
