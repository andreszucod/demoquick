from django.contrib import admin

from .models import Clients

@admin.register(Clients)
class ClientAdmin(admin.ModelAdmin):
	list_display = ('id', 'document', 'email', 'useremail')
	search_fields = ('document', 'email')
	list_per_page = 10
