from django.db import models
from rest_framework.reverse import reverse
from decimal import Decimal

from taggit.managers import TaggableManager

from products.utils import category_file_name, product_file_name, product_secondary_image_name


# Create your models here.


class ProductCategory(models.Model):
    category = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(
        upload_to=category_file_name,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('category',)
        verbose_name = 'category'
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse(
            'products:category',
            args=[
                self.slug
            ])


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    tags = TaggableManager()
    branch = models.ForeignKey('businesses.BusinessBranch', related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=product_file_name,
        blank=True,
        null=True,
    )
    description = models.TextField(blank=True, null=True)
    additional_info = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    @property
    def discount(self, rate=25):
        return "%.2f" % (self.price * Decimal((100 + rate) / 100))

    def get_absolute_url(self):
        return reverse(
            'shop:product_detail',
            args=[
                self.branch.business.slug,
                self.branch.slug,
                self.slug
            ]
        )


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(
        upload_to=product_secondary_image_name,
        blank=False,
        null=False,
    )
