from django.db import models


class Products(models.Model):
    id = models.AutoField(
        primary_key=True)
    name = models.CharField(
        max_length=30, 
        blank=True,
        verbose_name='Nombre Producto')
    descripcion = models.CharField(
        max_length=256, 
        blank=True,
        verbose_name='Descripcion')
    atributo4 = models.CharField(
        max_length=64, 
        blank=True,
        verbose_name='Atributo 4')

    
    class Meta:
      db_table = 'products'
      verbose_name_plural = "Productos"

    def __str__(self):
        return '{} {} {}'.format(self.id, self.name, self.descripcion)