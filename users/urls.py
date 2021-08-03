from users.models import Permission
from django.urls import path
from .views import PermissionAPIView, RoleViewSet, login, register, AuthenticatedUser, logout

urlpatterns = [
    path('register', register),
    path('login', login),
    path( 'user', AuthenticatedUser.as_view()),
    path('logout', logout),
    path( 'permissions', PermissionAPIView.as_view()),
    path('roles', RoleViewSet.as_view({
        'get': "list",
        'post': 'create',
    })),
    path('roles/<str:pk>', RoleViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    }))
]
