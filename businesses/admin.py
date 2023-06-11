from django.contrib import admin

from .models import BusinessCategory, BusinessBranch, BusinessCatalog


# Register your models here.


@admin.register(BusinessCategory)
class BusinessCategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'slug', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('category',)}
    list_filter = ['created_at', 'updated_at']
    search_fields = ['category', 'slug']
    date_hierarchy = 'created_at'
    list_editable = ['slug']


class BusinessBranchInline(admin.TabularInline):
    prepopulated_fields = {'slug': ('name',)}
    model = BusinessBranch


@admin.register(BusinessCatalog)
class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'owner', 'address', 'is_approved', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_approved']
    inlines = [BusinessBranchInline]
