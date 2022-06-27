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
from .serializers import BillSerializers

# Importar el modelo
from .models import Bills

#---------------------------------------------------------------------

# Clase para listar elementos de una Api
class BillListView(ListAPIView):
    # Serializador a usar
    serializer_class = BillSerializers
    # Valida que el usuario este autenticado para ingresar a la vista
    # Se pueden generar los permisos localmente o de manera global en el base.py
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Bills.objects.all()

# Clase para crear un elemento mediante una Api
class BillCreateView(CreateAPIView):
    # Serializador a usar
    serializer_class = BillSerializers


# Clase mostrar en detalle un elemento en particular mediante una Api
class BillDetailView(RetrieveAPIView):
    # Serializador a usar
    serializer_class = BillSerializers
    # Consulta que trae o filtra los datos
    queryset = Bills.objects.all()


# Clase para borrar  un elemento en particular mediante una Api
class BillDeleteView(DestroyAPIView):
    # Serializador a usar
    serializer_class = BillSerializers
    # Consulta que trae o filtra los datos
    queryset = Bills.objects.all()


# Clase para Actualizar  un elemento en particular mediante una Api CON DATOS
class BillRetrieveUpdateView(RetrieveUpdateAPIView):
    # Serializador a usar
    serializer_class = BillSerializers
    # Consulta que trae o filtra los datos
    queryset = Bills.objects.all()
