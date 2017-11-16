from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from products.models import Product

# Create your models here.
class Order (models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return 'Order{}'.format(self.id)

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())

	


class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items')
	product = models.ForeignKey(Product, related_name='order_items')
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return'{}'.format(self.id)

	def get_cost(self):
		return self.price * self.quantity

def order_created(order_id):
		"""
		Task to send email notification when an order is successfully created
		"""
		order = Order.objects.get(id=order_id)
		subject = 'Order nr.{}'.format(order_id)
		message = 'Dear {},\n\nYou have successfully placed an order for stock footage. Your order id is {}.'.format(order.first_name, order.id)
		mail_sent = send_mail(subject, message, "maaisiexx@gmail.com", [order.email])
		return mail_sent

