from django.shortcuts import render
from .models import Page

# Create your views here.
def page(request, slug):

    # Seleccionamos los datos de la página usando el SLUG que nos llega
    page = Page.objects.get(slug=slug) # Equivale a SELECT * FROM Page WHERE...

    return render(request, 'pages/page.html', {
        'page': page
    })
