from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class Usuario(AbstractUser):
    imagen = models.ImageField(upload_to='usuarios', null=True, blank=True, default='usuario/user-default.jpg')

    def get_absolute_url(self):
        return reverse('index')

