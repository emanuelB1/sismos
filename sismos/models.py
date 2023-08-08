from django.db import models


class Sismo(models.Model):
    fecha = models.DateTimeField()
    profundidad = models.CharField(max_length=10)
    magnitud = models.CharField(max_length=10)
    ref_geografica = models.CharField(max_length=100)
    fecha_update = models.DateTimeField()

    def __str__(self):
        return f"Sismo: {self.magnitud} - {self.fecha}"
