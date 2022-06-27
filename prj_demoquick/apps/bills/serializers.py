# Importar la funcionalidad de serializar
from rest_framework import serializers

from .models import Bills

# Importar el serializador de Client
from apps.clients.serializers import ClientSerializers
from apps.products.serializers import ProductSerializers


class BillSerializers(serializers.ModelSerializer):

    # Trae los datos serializados del modelo Client
    client_id = ClientSerializers()
    # Trae los datos serializados del modelo Product
    bills_products = ProductSerializers(many=True)

    class Meta:
        model = Bills
        fields = (
            'id',
            # Relaciona el modelo Clients ForeignKey
            'client_id',
            'company_name',
            'nit',
            'code',
            # Relaciona el modelo Products ManyToMany
            'bills_products',
        )