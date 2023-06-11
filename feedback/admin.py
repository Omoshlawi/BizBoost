from django.contrib import admin

from feedback.models import BusinessReview, BusinessContact


# Register your models here.

@admin.register(BusinessReview)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['user', 'branch', 'rating', 'created_at', 'updated_at', 'review']
    list_filter = ['user', 'created_at', 'updated_at', 'rating', 'branch']
    list_editable = ['rating', 'branch']


@admin.register(BusinessContact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'message', 'created_at', 'is_addressed', 'business')
