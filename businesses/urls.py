from rest_framework import routers
from django.urls import path

from .views import BusinessCatalogViewSet, BusinessCategoryViewSet, BusinessBranchViewSet
app_name = 'businesses'

router = routers.DefaultRouter()
router.register(prefix='categories', viewset=BusinessCategoryViewSet, basename='category')
router.register(prefix='branches', viewset=BusinessBranchViewSet, basename='branch')
router.register(prefix='', viewset=BusinessCatalogViewSet, basename='business')


urlpatterns = router.urls
