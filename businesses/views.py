from django.shortcuts import render
from rest_framework import viewsets

from .models import BusinessCategory, BusinessCatalog, BusinessBranch
from .serializers import BusinessCategorySerializer, BusinessCatalogSerializer, BusinessBranchSerializer


# Create your views here.


class BusinessCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = BusinessCategorySerializer
    queryset = BusinessCategory.objects.all()


class BusinessCatalogViewSet(viewsets.ModelViewSet):
    serializer_class = BusinessCatalogSerializer
    queryset = BusinessCatalog.objects.filter(is_approved=True)


class BusinessBranchViewSet(viewsets.ModelViewSet):
    serializer_class = BusinessBranchSerializer
    queryset = BusinessBranch.objects.filter(is_approved=True)
