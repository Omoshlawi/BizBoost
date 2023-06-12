from rest_framework import serializers

from businesses.models import BusinessCategory, BusinessCatalog, BusinessBranch


class BusinessCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BusinessCategory
        fields = ('id', 'url', 'category', 'slug', 'image', 'marker', 'created_at', 'updated_at')
        extra_kwargs = {
            'url': {'view_name': 'businesses:category-detail'},
        }


class BusinessCatalogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BusinessCatalog
        fields = (
            'id', 'url',
            'name', 'slug', 'owner', 'longitude', 'latitude', 'address',
            'created_at', 'updated_at', 'description',
            'additional_info', 'is_approved', 'image'
        )
        extra_kwargs = {
            'url': {'view_name': 'businesses:business'},
            'owner': {'view_name': 'users:user-detail'},
        }


class BusinessBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessBranch
        fields = (
            'id', 'url', 'business', 'name', 'category', 'customer_service_number',
            'slug', 'longitude', 'latitude', 'address', 'created_at', 'updated_at',
            'description', 'additional_info', 'image', 'is_approved'
        )
        extra_kwargs = {
            'url': {'view_name': 'businesses:branch-list'},
            'business': {'view_name': 'businesses:business-detail'},
            'category': {'view_name': 'businesses:category-detail'}
        }
