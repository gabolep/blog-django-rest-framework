from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #SI QUIERO CREAR UN SUPERUSER TENGO Q COMENTAR ESTAS LINEAS
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    