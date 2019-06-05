import jwt

from django.conf import settings


def get_review_token(reviewer, page_revision):
    payload = {
        'reviewer_id': reviewer.id,
        'page_revision_id': page_revision.id,
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
