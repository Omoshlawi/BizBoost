from django.db import models


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.id}'

    @property
    def paid(self):
        return self.payment.completed

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    @property
    def amount_paid(self):
        return self.payment.amount_paid

    @property
    def total_cost(self):
        return sum(item.cost for item in self.items.all())

    @property
    def balance(self):
        return self.total_cost - self.amount_paid

    @property
    def order_id(self):
        return f"ORD-{self.id}-{self.created_at.year}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='product')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.product)

    @property
    def cost(self):
        return self.price * self.quantity

