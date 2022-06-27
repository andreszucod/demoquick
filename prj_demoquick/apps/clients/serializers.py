# Importar la funcionalidad de serializar
from rest_framework import serializers

from .models import Clients


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = (
            'id',
            'document',
            'first_name',
            'last_name',
            'email',
            # Relaciona el modelo User ForeignKey
            'useremail',
        )