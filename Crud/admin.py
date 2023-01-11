from django.contrib import admin
from .models import usuarios
from .models import profesores
from .models import alumnos
from .models import tpi
from .models import carrera
from .models import pais
from .models import provincia
from .models import ciudad

# Register your models here.

admin.site.register(usuarios)
admin.site.register(profesores)
admin.site.register(alumnos)
admin.site.register(tpi)
admin.site.register(carrera)
admin.site.register(pais)
admin.site.register(provincia)
admin.site.register(ciudad)

