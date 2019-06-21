from rest_framework import serializers

from ..api.serializers import ReviewerSerializer

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
