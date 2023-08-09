import requests
from .models import Sismo
from django.utils import timezone
from datetime import datetime
from .models import Sismo

def consumir_api_guardar_sismos():
    url = "https://api.xor.cl/sismo/recent"  # Reemplaza con la URL de la nueva API de sismos
    response = requests.get(url)
    if response.status_code == 200:
        sismos_data = response.json()['events']
        for sismo_data in sismos_data:
            fecha = sismo_data['local_date']
            fecha_obj = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
            fecha_con_zona_horaria = timezone.make_aware(fecha_obj)
            if not Sismo.objects.filter(fecha=fecha_con_zona_horaria).exists():
                magnitude_data = sismo_data['magnitude']
                Sismo.objects.create(
                    fecha=fecha_con_zona_horaria,  # Utiliza la fecha con zona horaria
                    profundidad=str(sismo_data['depth']),
                    magnitud=str(magnitude_data['value']),
                    ref_geografica=sismo_data['geo_reference'],
                    latitud=sismo_data['latitude'],
                    longitud=sismo_data['longitude']
                )