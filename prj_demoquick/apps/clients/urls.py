from django.urls import path

from . import views

app_name = 'clients_apps'

urlpatterns = [
    path(
        'api/clients/list/',
        views.ClientListView.as_view(),
    ),
    path(
        'api/clients/create/',
        views.ClientCreateView.as_view(),
    ),
    path(
        'api/clients/detail/<pk>/',
        views.ClientDetailView.as_view(),
    ),
    path(
        'api/clients/delete/<pk>/',
        views.ClientDeleteView.as_view(),
    ),
    path(
        'api/clients/modify/<pk>/',
        views.ClientRetrieveUpdateView.as_view(),
    ),
]