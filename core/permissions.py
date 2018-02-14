from rest_framework import permissions


class DraftTokenPermisison(permissions.BasePermission):

    TOKEN_PARAM = 'draft_token'

    def has_object_permission(self, request, view, obj):
        return obj.specific.is_draft_token_valid(
            request.GET.get(self.TOKEN_PARAM, '')
        )
