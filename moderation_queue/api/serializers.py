from rest_framework import serializers

from ..models import ModeratorReview


class ModeratorReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeratorReview
        fields = [
            'comment',
            'is_accepted',
        ]
