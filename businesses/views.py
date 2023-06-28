from django.shortcuts import render
from django.utils.text import slugify
from rest_framework import viewsets

from .mixins.views import BusinessMixin
from .models import BusinessCategory, BusinessCatalog, BusinessBranch
from .serializers import BusinessCategorySerializer, BusinessCatalogSerializer, BusinessBranchSerializer


# Create your views here.


class BusinessCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = BusinessCategorySerializer
    queryset = BusinessCategory.objects.all()


class BusinessCatalogViewSet(viewsets.ModelViewSet, BusinessMixin):
    serializer_class = BusinessCatalogSerializer
    queryset = BusinessCatalog.objects.filter(is_approved=True)

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        slug = slugify(f'{name}')
        serializer.save(slug=slug)

    def perform_update(self, serializer):
        self.perform_create(serializer)


class BusinessBranchViewSet(viewsets.ModelViewSet):
    serializer_class = BusinessBranchSerializer
    queryset = BusinessBranch.objects.filter(is_approved=True)
