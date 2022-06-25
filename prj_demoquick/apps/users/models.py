from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Se crea el manager que define los parametrso que usara el nuevo modelo users
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    id = models.AutoField(
        primary_key=True)
    document = models.IntegerField(
        verbose_name='Documento',
        null=True,
        blank=True)
    first_name = models.CharField(
        max_length=30, 
        blank=True,
        verbose_name='Nombres')
    last_name = models.CharField(
        max_length=30, 
        blank=True,
        verbose_name='Apellidos')
    email = models.EmailField(
        unique=True,
        verbose_name='Email')
    # El username se deja NO obligatorio
    username = models.CharField(
        max_length=20, 
        blank=True,
        verbose_name='Usuario')
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    # Definir que campos se requieren para la creacion del usuario
    #REQUIRED_FIELDS = ['email',]
    
    #Variable de objeto que permite usar el manager
    objects = UserManager()

    def get_short_name (self):
        return self.first_name

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name