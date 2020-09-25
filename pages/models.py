from django.db import models

# Create your models here.

# Modelo para las páginas
class Page(models.Model):

    # Campos de la página
    title = models.CharField(max_length=50, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    slug = models.CharField(unique=True, max_length=150, verbose_name='URL amigable')
    visible = models.BooleanField(verbose_name='¿Visible?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creada el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizada el')

    # Clase meta para configurar parámetros
    class Meta:

        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'

    # Método para que imprima el título de la página como un String
    def __str__(self):
        return self.title
    


