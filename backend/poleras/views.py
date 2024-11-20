from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Definir una lista de poleras directamente en el archivo views.py
poleras = [
    {'nombre': 'Polera Rojo', 'descripcion': 'Polera de color rojo, talla M'},
    {'nombre': 'Polera Azul', 'descripcion': 'Polera de color azul, talla L'},
    {'nombre': 'Polera Verde', 'descripcion': 'Polera de color verde, talla S'},
]

# Vista protegida por login_required
@login_required
def lista_poleras(request):
    return render(request, 'poleras/poleras.html', {'poleras': poleras})

