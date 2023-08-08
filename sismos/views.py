from django.shortcuts import render
from .models import Sismo
from .utils import consumir_api_guardar_sismos
from datetime import datetime


def lista_sismos(request):
    consumir_api_guardar_sismos()
    sismos = Sismo.objects.all()
    return render(request, 'index.html', {'sismos': sismos})

def busqueda(request):
    if request.method == 'POST':
        fecha_busqueda = request.POST.get('fecha_busqueda')
        try:
            fecha = datetime.strptime(fecha_busqueda, '%Y-%m-%d')
            sismos = Sismo.objects.filter(fecha__date=fecha.date())
        except ValueError:
            sismos = Sismo.objects.all()
    else:
        sismos = Sismo.objects.all()

    return render(request, 'resultados.html', {'sismos': sismos})
