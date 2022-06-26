
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
    RetrieveUpdateAPIView

    )

from .serializers import ProductSerializers

from .models import Products

# Clase para listar elementos de una Api
class ProductListView(ListAPIView):
    # Serializador a usar
    serializer_class = ProductSerializers

    def get_queryset(self):
        return Products.objects.all()

# Clase para crear un elemento mediante una Api
class ProductCreateView(CreateAPIView):
    # Serializador a usar
    serializer_class = ProductSerializers


# Clase mostrar en detalle un elemento en particular mediante una Api
class ProductDetailView(RetrieveAPIView):
    # Serializador a usar
    serializer_class = ProductSerializers
    # Consulta que trae o filtra los datos
    queryset = Products.objects.all()


# Clase para borrar  un elemento en particular mediante una Api
class ProductDeleteView(DestroyAPIView):
    # Serializador a usar
    serializer_class = ProductSerializers
    # Consulta que trae o filtra los datos
    queryset = Products.objects.all()


# Clase para Actualizar  un elemento en particular mediante una Api sin los datos
class ProductUpdateView(UpdateAPIView):
    # Serializador a usar
    serializer_class = ProductSerializers
    # Consulta que trae o filtra los datos
    queryset = Products.objects.all()


# Clase para Actualizar  un elemento en particular mediante una Api CON DATOS
class ProductRetrieveUpdateView(RetrieveUpdateAPIView):
    # Serializador a usar
    serializer_class = ProductSerializers
    # Consulta que trae o filtra los datos
    queryset = Products.objects.all()
