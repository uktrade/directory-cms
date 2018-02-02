from sigauth import permissions

from django.conf import settings


class SignatureCheckPermission(permissions.SignatureCheckPermissionBase):
    secret = settings.SIGNATURE_SECRET
