from rest_framework.permissions import BasePermission
from .models import User


class IsAdministrador(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.role == User.Role.ADMINISTRADOR
        )


class IsOperadorOrAdministrador(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.role in (User.Role.OPERADOR, User.Role.ADMINISTRADOR)
        )
