from django.shortcuts import render
from rest_framework.reverse import reverse_lazy
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions


# Create your views here.


class ApiRootView(APIView):
    def get(self, request):
        return Response({
            'users_url': reverse_lazy("users:user-list", request=request),
            'current_user_url': reverse_lazy('users:user-detail', args=[':id'], request=request),
            'business_catalogs_url': reverse_lazy('businesses:business-list', request=request),
            'business_catalog_url': reverse_lazy('businesses:business-detail', args=[':id'], request=request),
            'business_categories_url': reverse_lazy('businesses:category-list', request=request),
            'business_category_url': reverse_lazy('businesses:category-detail', args=[':id'], request=request),
            'business_branches_url': reverse_lazy('businesses:branch-list', request=request),
            'business_branch_url': reverse_lazy('businesses:branch-detail', args=[':id'], request=request),
        })
