from django import forms
from django.db import models

# Create your models here.
class Signup(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=255)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

