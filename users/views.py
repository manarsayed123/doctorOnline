from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework import permissions

from users.models import Profile
from users.serializers import UserListSerializer, UserSerializer
from rest_framework.response import Response


class Registeration(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if request.data.get('role') not in [k for k, v in Profile.role_choices]:
            raise ValidationError("please add valid role")

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.set_password(request.data['password'])
            Profile.objects.create(user=user, role=request.data.get('role', None))
            return Response(UserListSerializer(user).data)
