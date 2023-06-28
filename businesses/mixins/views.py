from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from businesses.models import BusinessCatalog


class BusinessMixin:
    @action(
        detail=False,
        permission_classes=[permissions.IsAuthenticated],
        queryset=BusinessCatalog.objects.all()
    )
    def my_business(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)