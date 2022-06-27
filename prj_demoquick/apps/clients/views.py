#Importar librerias para generar el csv
import csv
from urllib import response
from django.http import HttpResponse
from rest_framework.views import APIView

# Habiliatmos el DRF
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    # Listar detalladamente un registro
    RetrieveAPIView,
    # Borrar un registro 
    DestroyAPIView,
    # Modificar o Actualizar un registro con los campos en blanco
    UpdateAPIView,
    # Modificar o Actualizar un registro trae los datos
    RetrieveUpdateAPIView,
    )

# Importar la libreria de permisos para la validacion del JWT
from rest_framework.permissions import IsAuthenticated

# Importar el serializador a la vista
from .serializers import ClientSerializers

# Importar el modelo
from .models import Clients

#---------------------------------------------------------------------

# Clase para listar elementos de una Api
class ClientListView(ListAPIView):
    # Serializador a usar
    serializer_class = ClientSerializers
    # Valida que el usuario este autenticado para ingresar a la vista
    # Se pueden generar los permisos localmente o de manera global en el base.py
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Clients.objects.all()

# Clase para crear un elemento mediante una Api
class ClientCreateView(CreateAPIView):
    # Serializador a usar
    serializer_class = ClientSerializers


# Clase mostrar en detalle un elemento en particular mediante una Api
class ClientDetailView(RetrieveAPIView):
    # Serializador a usar
    serializer_class = ClientSerializers
    # Consulta que trae o filtra los datos
    queryset = Clients.objects.all()


# Clase para borrar  un elemento en particular mediante una Api
class ClientDeleteView(DestroyAPIView):
    # Serializador a usar
    serializer_class = ClientSerializers
    # Consulta que trae o filtra los datos
    queryset = Clients.objects.all()


# Clase para Actualizar  un elemento en particular mediante una Api CON DATOS
class ClientRetrieveUpdateView(RetrieveUpdateAPIView):
    # Serializador a usar
    serializer_class = ClientSerializers
    # Consulta que trae o filtra los datos
    queryset = Clients.objects.all()

# Generar la salida CSV
class ExportCSVClients(APIView):
    def get(self, request, *arg, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachmemt; filename="export.csv"'

        writer = csv.writer(response)

        for student in Clients.objects.all():
            row = ','.join([
                id,
                document,
                email,
            ])

            writer.writerow(row)
        
        return response