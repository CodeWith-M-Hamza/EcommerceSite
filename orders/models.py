from django.db import models

from products.models import Product  # Assuming you have a Product model in products app







class Order(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    paid=models.BooleanField(default=False)
    # def get_total_cost(self):
    #     return sum(item.get_cost() for item in self.items.all())
    def get_total_cost(self):
        return sum((item.get_cost() or 0) for item in self.items.all())

class OrderItem(models.Model):
    order=models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product=models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)
    def get_cost(self):
        return self.price * self.quantity