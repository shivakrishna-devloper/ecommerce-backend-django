from rest_framework.permissions import BasePermission, SAFE_METHODS

# Custom permission:
# - Admins can do anything
# - Others can only READ
class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        # SAFE_METHODS = GET, HEAD, OPTIONS
        if request.method in SAFE_METHODS:
            return True

        # Only admin users can modify data
        return request.user.role == 'admin'