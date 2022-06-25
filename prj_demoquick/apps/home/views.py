from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Pagina de llegada
def IndexView(request):
    return render(request, 'home/index.html')

# Pagina de Seleccion de mapa a ingresar
@login_required
def Menu1View(request):
    return render(request, 'home/menu1.html')