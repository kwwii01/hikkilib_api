from rest_framework.permissions import BasePermission


class IsCommentOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        res = (obj.profile.user == request.user) or request.user.is_superuser
        print(res)
        return res
