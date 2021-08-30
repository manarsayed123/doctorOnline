from rest_framework.permissions import BasePermission

from users.models import Profile


class IsDoctor(BasePermission):
    """
    Allows access only to doctors.
    """

    def has_permission(self, request, view):
        if hasattr(request.user, 'user_profile'):
            return bool(request.user and request.user.user_profile.role == Profile.DOCTOR)
        else:
            return False


class IsPatient(BasePermission):
    """
    Allows access only to patients.
    """

    def has_permission(self, request, view):
        if hasattr(request.user, 'user_profile'):

            return bool(request.user and request.user.user_profile.role == Profile.PATIENT)
        else:
            return False
