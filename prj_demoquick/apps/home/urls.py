from django.urls import path

from apps.home import views


app_name = 'home_app'   

urlpatterns = [
    path(
        '',
        views.IndexView,
        name='view-index',
    ),
    path(
        'menu1/',
        views.Menu1View,
        name='view-menu1',
    ),
]