from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField()
    customer_phno = models.CharField(max_length=30)
    customer_place = models.CharField(max_length=50)
    customer_password = models.CharField(max_length=50)