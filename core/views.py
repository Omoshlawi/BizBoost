from django.shortcuts import render
from rest_framework import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
# Create your views here.


class ApiRootView(APIView):
    def get(self, request):
        return Response({})
