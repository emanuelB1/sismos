import requests
from .models import Sismo


def consumir_api_guardar_sismos():
    url = "https://api.gael.cloud/general/public/sismos"  # Reemplaza con la URL de la API de sismos
    response = requests.get(url)
    if response.status_code == 200:
        sismos_data = response.json()
        for sismo_data in sismos_data:
            fecha = sismo_data['Fecha']
            if not Sismo.objects.filter(fecha=fecha).exists():
                Sismo.objects.create(
                    fecha=fecha,
                    profundidad=sismo_data['Profundidad'],
                    magnitud=sismo_data['Magnitud'],
                    ref_geografica=sismo_data['RefGeografica'],
                    fecha_update=sismo_data['FechaUpdate']
                )
