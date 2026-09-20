from django.contrib import admin
from .models import Empresa, Conductor, Licencia, Ruta

# Registramos todos nuestros modelos en el panel de control
admin.site.register(Empresa)
admin.site.register(Conductor)
admin.site.register(Licencia)
admin.site.register(Ruta)