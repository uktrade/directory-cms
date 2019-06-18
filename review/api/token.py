import jwt

from django.conf import settings


def get_review_token(reviewer, page_revision, enable_moderation=False):
    payload = {
        'reviewer_id': reviewer.id,
        'page_revision_id': page_revision.id,
        'reviewer_name': reviewer.get_name(),
        'moderation_enabled': enable_moderation,
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
