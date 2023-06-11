from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
from django.urls import reverse
import os

from .utils import bs_category_file_name, markers_file_name, business_file_name, business_branch_file_name

RATING_CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
]


class BusinessCategory(models.Model):
    category = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(
        upload_to=bs_category_file_name,
        blank=True,
        null=True,
    )
    marker = models.ImageField(
        upload_to=markers_file_name,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'category'
        verbose_name_plural = 'Business Categories'

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('business:category', args=[self.slug])


class BusinessCatalog(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, db_index=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    address = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to=business_file_name,
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse(
            'business:own_business_detailed',
            args=[self.slug]
        )

    def __str__(self):
        return self.name

    @property
    def location(self):
        return f"{self.latitude}, {self.longitude}"


class BusinessBranch(models.Model):
    business = models.ForeignKey(BusinessCatalog, on_delete=models.CASCADE, related_name="branch")
    name = models.CharField(max_length=100)
    category = models.ForeignKey(BusinessCategory, related_name='businesses', on_delete=models.CASCADE)
    customer_service_number = PhoneNumberField(null=True, blank=True)
    slug = models.SlugField(db_index=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    address = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to=business_branch_file_name,
        blank=True,
        null=True
    )
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def location(self):
        return f"{self.latitude}, {self.longitude}"

    def get_absolute_url(self):
        return reverse(
            'shop:shop',
            args=[
                self.business.slug,
                self.slug
            ]
        )


