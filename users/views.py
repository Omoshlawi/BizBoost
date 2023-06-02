from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets

from users.mixins import AuthMixin
from users.serializers import UserSerializer


# Create your views here.
class UserViewSet(
    viewsets.ModelViewSet,
    AuthMixin,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
