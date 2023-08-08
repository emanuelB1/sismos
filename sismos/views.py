from django.shortcuts import render
from .models import Sismo
from .utils import consumir_api_guardar_sismos
from datetime import datetime, date


def lista_sismos(request):
    consumir_api_guardar_sismos()
    fecha_actual = date.today()
    sismos = Sismo.objects.filter(fecha__date=fecha_actual).order_by('-fecha')
    return render(request, 'index.html', {'sismos': sismos})

def busqueda(request):
    fecha_actual = date.today()
    if request.method == 'POST':
        fecha_busqueda = request.POST.get('fecha_busqueda')
        try:
            fecha = datetime.strptime(fecha_busqueda, '%Y-%m-%d')
            sismos = Sismo.objects.filter(fecha__date=fecha.date()).order_by('-fecha')
        except ValueError:
            sismos = Sismo.objects.filter(fecha__date=fecha_actual).order_by('-fecha')
    else:
        sismos = Sismo.objects.filter(fecha__date=fecha_actual).order_by('-fecha')

    return render(request, 'index.html', {'sismos': sismos})
