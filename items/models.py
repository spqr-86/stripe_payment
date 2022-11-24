from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_item_id = models.CharField(max_length=100)
    stripe_price_id = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}, {self.price} $'
