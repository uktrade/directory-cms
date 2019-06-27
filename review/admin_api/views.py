from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from wagtail.core.models import Page

from ..api.serializers import CommentSerializer

from .. import models
from . import serializers


class FooAuth(SessionAuthentication):
    # TODO: Make it work with CSRF
    def enforce_csrf(self, request):
        return


class AdminAPIViewMixin:
    authentication_classes = [FooAuth]

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PageShares(AdminAPIViewMixin, generics.ListCreateAPIView):
    serializer_class = serializers.ShareSerializer

    def get_queryset(self):
        page = get_object_or_404(Page, pk=self.kwargs['pk'])
        return models.Share.objects.filter(page_revision__page=page).order_by('shared_at')

    def create(self, *args, **kwargs):
        page = get_object_or_404(Page, pk=kwargs['pk'])

        serializer = serializers.NewShareSerializer(None, self.request.data)
        serializer.is_valid(raise_exception=True)

        # Look for a user with the email address
        email = serializer.data['email']
        User = get_user_model()
        user = User.objects.filter(email=email).first()

        if user is not None:
            reviewer, created = models.Reviewer.objects.get_or_create(user=user)
        else:
            reviewer, created = models.Reviewer.objects.get_or_create(email=email)

        if models.Share.objects.filter(page_revision__page=page, reviewer=reviewer).exists():
            raise ValidationError({'email': "This page has already been shared with this email address"})

        share = models.Share.objects.create(
            page_revision=page.get_latest_revision(),
            reviewer=reviewer,
            shared_by=self.request.user,
        )

        share.send_share_email()

        serializer = serializers.ShareSerializer(share)

        return Response(serializer.data, status=201)  # FIXME


class PageComments(AdminAPIViewMixin, generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        page = get_object_or_404(Page, pk=self.kwargs['pk'])
        return models.Comment.objects.filter(page_revision__page=page).order_by('-created_at')
