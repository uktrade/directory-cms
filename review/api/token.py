import jwt

from django.conf import settings


def get_review_token(reviewer, page_revision, enable_moderation=False, share_id=None):
    payload = {
        'reviewer_id': reviewer.id,
        'page_revision_id': page_revision.id,
        'reviewer_name': reviewer.get_name(),
    }

    if enable_moderation:
        payload['moderation_enabled'] = True

    if share_id is not None:
        payload['share_id'] = share_id

    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
