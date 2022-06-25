from django.db import models

from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):

    # definir una funcion privada, no accesible desde otra funcion o clase
    def _create_user(self, email, password, is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        # Encripta el password que se envia
        user.set_password(password)
        # Salva el password
        user.save(using=self.db)
        return user
    
    # Define la funcion para crear los usuarios
    def create_user(self, email, password=None, **extra_fields):
        return self._create_user( email, password, False, False, True, **extra_fields)

    # se define la funcion para el super pasandole parametros
    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user( email, password, True, True, True, **extra_fields)
    
    # def cod_validation(self, id_user, cod_registro):
    #     if self.filter(id=id_user, codregistro=cod_registro).exists():
    #         return True
    #     else:
    #         return False