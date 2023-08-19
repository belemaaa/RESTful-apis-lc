from rest_framework import permissions
from .permissions import IsStaffPermission


class StaffPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffPermission]