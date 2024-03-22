from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)
    username = models.CharField(max_length=10)
    location = models.CharField(max_length=30)
