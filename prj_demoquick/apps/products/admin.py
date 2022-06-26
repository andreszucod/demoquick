from django.contrib import admin

from .models import Products

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'descripcion', 'atributo4')
	search_fields = ('name', 'descripcion')
	list_per_page = 10
