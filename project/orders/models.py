from django.db import models
from items.models import Item


class Order(models.Model):
    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )
    item = models.OneToOneField(
        Item,
        related_name='order_items',
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.item.price * self.quantity

    def save(self, *args, **kwargs):
        self.price = self.item.price
        super().save(*args, **kwargs)
