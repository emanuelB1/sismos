import requests
from .models import Sismo


import requests
from .models import Sismo

def consumir_api_guardar_sismos():
    url = "https://api.xor.cl/sismo/recent"  # Reemplaza con la URL de la nueva API de sismos
    response = requests.get(url)
    if response.status_code == 200:
        sismos_data = response.json()['events']
        for sismo_data in sismos_data:
            fecha = sismo_data['local_date']
            if not Sismo.objects.filter(fecha=fecha).exists():
                magnitude_data = sismo_data['magnitude']
                Sismo.objects.create(
                    fecha=fecha,
                    profundidad=str(sismo_data['depth']),
                    magnitud=str(magnitude_data['value']),
                    ref_geografica=sismo_data['geo_reference'],
                    fecha_update=sismo_data['utc_date'],
                    latitud=sismo_data['latitude'],
                    longitud=sismo_data['longitude']
                )
