from django.contrib import admin
from .models import Page

# Register your models here.

# Agreamos el modelo para poder gestionarlo desde el panel de admin
admin.site.register(Page)

# Configuración panel de administración
title = 'Proyecto con Django'
subtitle = 'Panel del control'

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
