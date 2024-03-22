from django.contrib.auth.hashers import make_password
from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)
    username = models.CharField(max_length=10)
    location = models.CharField(max_length=30)

    @classmethod
    def create_user(cls, email, password, username, location):
        user = cls(email=email, password=make_password(password), username=username, location=location)
        user.save()
        return user