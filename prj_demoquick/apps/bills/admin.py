from django.contrib import admin

from .models import Bills

@admin.register(Bills)
class BillsAdmin(admin.ModelAdmin):
	list_display = ('id', 'client_id', 'company_name', 'nit', 'code')
	search_fields = ('client_id', 'company_name')
	list_per_page = 10
