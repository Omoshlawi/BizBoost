from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class BusinessReview(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    branch = models.ForeignKey(
        'businesses.BusinessBranch',
        related_name="business_reviews",
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)],
        default=4
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review = models.TextField()

    def __str__(self) -> str:
        return f"{self.user.get_full_name()}'s review"


class BusinessContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone_number = PhoneNumberField(null=True, blank=True)
    message = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_addressed = models.BooleanField(default=False)
    business = models.ForeignKey(
        'businesses.BusinessCatalog',
        related_name='contacts',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)


class ProductReview(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    review = models.TextField()
