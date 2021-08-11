from rest_framework import permissions

from .serializers import UserSerializer
class ViewPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        data = UserSerializer(request.user).data

        view_acess = any(p['name'] == 'view_' + view.permission_object for p in data['role']['permissions'])
        edit_acess = any(p['name'] == 'edit_' + view.permission_object for p in data['role']['permissions'])

        if request.method == 'GET':
            return view_acess or edit_acess

        return edit_acess