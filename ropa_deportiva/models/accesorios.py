from django.db import models

class Accesorio(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.nombre}--{self.precio}'
