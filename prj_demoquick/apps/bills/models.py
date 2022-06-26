from django.db import models

from apps.clients.models import Clients
from apps.products.models import Products

class Bills(models.Model):
    id = models.AutoField(
        primary_key=True)
    client_id = models.ForeignKey(
        Clients,
        on_delete=models.PROTECT, 
        verbose_name="Cliente",
        help_text="Ingrese Cliente")
    company_name = models.CharField(
        max_length=30, 
        blank=True,
        verbose_name='Compañia')
    nit = models.IntegerField(
        verbose_name='Nit',
        null=True,
        blank=True)
    code = models.IntegerField(
        verbose_name='Codigo',
        null=True,
        blank=True)
    
    # Crea la tabla de paso para la relacion muchos a muchos
    bills_products = models.ManyToManyField(Products, blank=True,)

    # Se crean registgros de creacion y modificacion de las facturas
    fecha_crea = models.DateTimeField(
        auto_now_add=True)
    fecha_actualiza = models.DateTimeField(
        auto_now=True)
    
    class Meta:
      db_table = 'bills'
      verbose_name_plural = "Facturas"

    def __str__(self):
        return '{} {} {} {}'.format(self.client_id, self.company_name, self.nit, self.code)