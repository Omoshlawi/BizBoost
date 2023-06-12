from django.contrib import admin

from .models import BusinessStaff, StaffPermission


# Register your models here.

@admin.register(BusinessStaff)
class BusinessStaffAdmin(admin.ModelAdmin):
    list_display = ('branch', 'user', 'title', 'created_at', 'updated_at')


@admin.register(StaffPermission)
class StaffPermissionAdmin(admin.ModelAdmin):
    list_display = ('staff', 'write_business', 'write_branch', 'write_product')
