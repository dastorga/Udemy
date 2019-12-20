from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    message = "No es propietario"

