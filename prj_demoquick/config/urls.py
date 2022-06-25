from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('apps.home.urls'), name='url-home'),
    re_path('user/', include('apps.users.urls'), name='url-user'),
]
