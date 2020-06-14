from django.db import models

# Create your models here.

class Product(models.Model):
	title 		= models.TextField()
	description = models.TextField()
	Price 		= models.TextField()
	summary     = models.TextField(default='this is cool')