from django.urls import path

from . import views

app_name = 'products_apps'

urlpatterns = [
    path(
        'api/products/list/',
        views.ProductListView.as_view(),
    ),
    path(
        'api/products/create/',
        views.ProductCreateView.as_view(),
    ),
    path(
        'api/products/detail/<pk>/',
        views.ProductDetailView.as_view(),
    ),
    path(
        'api/products/delete/<pk>/',
        views.ProductDeleteView.as_view(),
    ),
    path(
        'api/products/modify/<pk>/',
        views.ProductRetrieveUpdateView.as_view(),
    ),
]