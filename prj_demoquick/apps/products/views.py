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

# Importar decorador para la funcion de consulta 
from django.contrib.auth.decorators import login_required
# Importar el serializador para las funciones
from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.http import HttpResponse

# Importar el serializador a la vista
from .serializers import ProductSerializers

# Importar el modelo
from .models import Products

#---------------------------------------------------------------------

# Clase para listar elementos de una Api
class ProductListView(ListAPIView):
    # Serializador a usar
    serializer_class = ProductSerializers
    # Valida que el usuario este autenticado para ingresar a la vista
    # Se pueden generar los permisos localmente o de manera global en el base.py
    permission_classes = (IsAuthenticated,)

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


# Clase para Actualizar  un elemento en particular mediante una Api CON DATOS
class ProductRetrieveUpdateView(RetrieveUpdateAPIView):
    # Serializador a usar
    serializer_class = ProductSerializers
    # Consulta que trae o filtra los datos
    queryset = Products.objects.all()


# Definicion de funcion para construir una consulta a productos
@login_required
def products_datasets(request):
	data_products = serialize('json', 
                                Products.objects.all(),
                                fields=(
                                        'id',
                                        'name',
                                        'descripcion',
                                        'atributo4',
                                        ))
	return HttpResponse(data_products,content_type='json')
