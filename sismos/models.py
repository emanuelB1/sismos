from django.db import models

class Sismo(models.Model):
    fecha = models.DateTimeField()
    profundidad = models.FloatField()
    magnitud = models.FloatField()
    ref_geografica = models.CharField(max_length=100)
    fecha_update = models.DateTimeField()
    latitud = models.FloatField()  # Agregar campo para latitud
    longitud = models.FloatField()  # Agregar campo para longitud

    def __str__(self):
        return f"Sismo: {self.magnitud} - {self.fecha}"
