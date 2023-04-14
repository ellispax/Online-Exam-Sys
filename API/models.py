from django.db import models

# Create your models here.


class Userdetails(models.Model):
    national_id = models.CharField(max_length=12, unique=True)
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
