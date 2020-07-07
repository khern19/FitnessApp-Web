from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    first_name = models.CharField('First Name', blank=True, max_length=30)
    last_name = models.CharField('Last Name', blank=True, max_length=30)
    username = models.CharField(
        'Username', unique=True, blank=False, max_length=20)
    email = models.CharField('Email', unique=True, blank=True, max_length=70)
