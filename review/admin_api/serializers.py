from rest_framework import serializers

from ..api.serializers import CommentSerializer, ReviewerSerializer
from ..api.token import get_review_token

from .. import models


class NewShareSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ['email']


class ShareSerializer(serializers.ModelSerializer):
    reviewer = ReviewerSerializer()
    expires_at = serializers.ReadOnlyField(source='get_expires_at')

    class Meta:
        model = models.Share
        fields = ['id', 'reviewer', 'shared_by', 'shared_at', 'first_accessed_at', 'last_accessed_at', 'expires_at']


class CommentSerializerWithFrontendURL(CommentSerializer):
    def get_reviewer(self):
        if 'reviewer' not in self.context:
            reviewer, created = models.Reviewer.objects.get_or_create(user=self.context['request'].user)
            self.context['reviewer'] = reviewer

        return self.context['reviewer']

    def get_frontend_url(self, comment):
        review_token = get_review_token(self.get_reviewer(), comment.page_revision)
        return comment.page_revision.page.specific.get_url(is_draft=True) + '&review_token=' + review_token.decode('utf-8') + '&comment=' + str(comment.id)

    def to_representation(self, comment):
        data = super().to_representation(comment)
        data['frontend_url'] = self.get_frontend_url(comment)
        return data
