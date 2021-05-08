from django.db import models

# Create your models here.

class app_data(models.Model):
	
	name = models.CharField(max_length = 30)
	age = models.IntegerField()
	address = models.TextField()
	image = models.ImageField()