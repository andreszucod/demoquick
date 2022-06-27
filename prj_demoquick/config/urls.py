from django.contrib import admin
from django.urls import path, re_path, include

# Importar las vistas de JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    # URL que habilita el JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # URL de las apps locales
    re_path('', include('apps.home.urls'), name='url-home'),
    re_path('user/', include('apps.users.urls'), name='url-user'),
    re_path('', include('apps.products.urls'), name='api-products-json'),
    re_path('', include('apps.clients.urls'), name='api-clients-json'),
    re_path('', include('apps.bills.urls'), name='api-bills-json'),
   
]
