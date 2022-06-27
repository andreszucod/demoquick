from django.urls import path

from . import views

app_name = 'bills_apps'

urlpatterns = [
    path(
        'api/bills/list/',
        views.BillListView.as_view(),
    ),
    path(
        'api/bills/create/',
        views.BillCreateView.as_view(),
    ),
    path(
        'api/bills/detail/<pk>/',
        views.BillDetailView.as_view(),
    ),
    path(
        'api/bills/delete/<pk>/',
        views.BillDeleteView.as_view(),
    ),
    path(
        'api/bills/modify/<pk>/',
        views.BillRetrieveUpdateView.as_view(),
    ),
]