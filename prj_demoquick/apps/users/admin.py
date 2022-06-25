from django.contrib import admin

# Importar los modelos que se van a registrar en el Admin de Django
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'document', 'first_name', 'last_name', 'email', 'username', 'is_staff')
    search_fields = ('document', 'email', 'username')
    list_per_page = 20   
