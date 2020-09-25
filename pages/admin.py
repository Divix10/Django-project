from django.contrib import admin
from .models import Page

# Register your models here.

# Agreamos el modelo para poder gestionarlo desde el panel de admin
admin.site.register(Page)
