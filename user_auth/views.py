from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
)

from .serializers import (
    RegisterSerializer,
    ChangePasswordSerializer,
    UserProfileSerializer,
)

# Create your views here.


class RegisterView(CreateAPIView):
    """
    API for the registration of user
    """
    permission_class = (IsAuthenticated,)
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


class ChangePasswordView(UpdateAPIView):
    """
    API for the change password of user
    """
    permission_class = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
    model = User

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({"msg": "Success."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(viewsets.ModelViewSet):
    permission_class = (IsAuthenticated,)
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        print(f'username is {self.request.user.username}')
        user = User.objects.filter(username=self.request.user.username)
        return user

