from django.contrib import admin

from services.models import ServiceCategory, Service


# Register your models here.


@admin.register(ServiceCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'slug', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('category',)}
    list_filter = ['created_at', 'updated_at']
    search_fields = ['category', 'slug']
    date_hierarchy = 'created_at'
    list_editable = ['slug']


@admin.register(Service)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}
