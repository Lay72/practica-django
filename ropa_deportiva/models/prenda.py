from django.db import models

# Create your models here.
class Prenda(models.Model):
    SIZE_CHOICES = (
        ('s', 'Small'),
        ('m', 'Medium'),
        ('l', 'Large'),
        ('xl', 'Extra Large'),
    )
    
    talla = models.CharField(max_length=10, choices=SIZE_CHOICES)
    tela = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Talla: {self.talla}, Precio: ${self.precio}"
