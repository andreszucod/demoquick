from django.db import models

from apps.users.models import User

class Clients(models.Model):
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
    useremail = models.ForeignKey(
        User,
        on_delete=models.PROTECT, 
        verbose_name="Usuario",
        help_text="Ingrese Usuario")
    
    class Meta:
      db_table = 'clients'
      verbose_name_plural = "Clientes"

    def __str__(self):
        return '{} {} {}'.format(self.id, self.email, self.useremail)