from rest_framework import serializers

from .. import models


class ReviewerSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='get_name')

    class Meta:
        model = models.CommentReply
        fields = ['name']


class CommentReplySerializer(serializers.ModelSerializer):
    reviewer = ReviewerSerializer()

    class Meta:
        model = models.CommentReply
        fields = ['reviewer', 'text', 'created_at', 'updated_at']


class CommentLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = ['content_path', 'start_xpath', 'start_offset', 'end_xpath', 'end_offset']


class CommentSerializer(serializers.ModelSerializer):
    reviewer = ReviewerSerializer(read_only=True)
    replies = CommentReplySerializer(many=True, read_only=True)

    class Meta:
        model = models.Comment
        fields = ['id', 'reviewer', 'quote', 'text', 'created_at', 'updated_at', 'is_resolved', 'replies', 'content_path', 'start_xpath', 'start_offset', 'end_xpath', 'end_offset']
