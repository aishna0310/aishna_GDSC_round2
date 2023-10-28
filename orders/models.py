from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Order(models.Model):
	product_name = models.CharField(max_length = 100)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	priority = models.CharField(max_length=50)

	def __str__(self):
		return self.product_name


	def get_absolute_url(self):
		return reverse('order-detail', kwargs={'pk': self.pk})


