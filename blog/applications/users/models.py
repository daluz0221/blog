from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


from .managers import UserManager
# Create your models here.


class User(AbstractUser, PermissionsMixin):
    
    

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    genero = models.CharField(max_length=1, choices=(('M', 'Masculino'), ('F', 'Femenino'), ("O", "Otros")), blank=True, null=True)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    objects = UserManager()

    def __str__(self):
        return self.username


