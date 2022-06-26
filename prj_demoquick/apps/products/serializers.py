# Importar la funcionalidad de serializar
from rest_framework import serializers

from .models import Products


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = (
            'id',
            'name',
            'descripcion',
            'atributo4',
        )

