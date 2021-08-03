from users.authentication import gernerate_acess_token
from users.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions, serializers
from rest_framework.views import APIView

from .serializers import UserSerializer
from .models import User
from .authentication import gernerate_acess_token

@api_view(['POST'])
def register(request):
    data = request.data

    if data['password'] != data['password_confirm']:
        raise exceptions.APIException('Passwords do not match.')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()

    if user is None:
        raise exceptions.AuthenticationFailed('user not found')
    
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('incorrect password')

    response = Response()

    token = gernerate_acess_token(user)
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }

    return response

class AuthenticatedUser(APIView):
    authentication_classes = []
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)

        return Response({
            'data': serializer.data
        })




@api_view(['GET'])
def users(request):
    serializer = UserSerializer(User.objects.all(), many=True)
    return Response(serializer.data)

