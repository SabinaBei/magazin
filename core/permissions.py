from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions

class ProductPermission(permissions.BasePermission):
    # message = 'Adding customers not allowed.'

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.user != AnonymousUser:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        else:
            if obj.user == request.user:
                return True