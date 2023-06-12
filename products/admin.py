from django.contrib import admin

# Register your models here.

from .models import ProductCategory, Product, ProductImage


@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'slug', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('category',)}
    list_filter = ['created_at', 'updated_at']
    search_fields = ['category', 'slug']
    date_hierarchy = 'created_at'
    list_editable = ['slug']


class ProductImagesInline(admin.TabularInline):
    model = ProductImage
    raw_id_fields = ['product']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImagesInline]
