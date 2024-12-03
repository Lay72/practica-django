from django.contrib import admin

# Register your models here.
from .models.prenda import Prenda 
from .models.accesorios import Accesorio 
admin.site.register(Prenda)
admin.site.register(Accesorio)