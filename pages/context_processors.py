from pages.models import Page

# Función que selecciona todas las páginas para poder ser usadas en cualquier template
def get_pages(request):

    # Seleccionamos en la BD los atributos de la página
    pages = Page.objects.filter(visible=True).values_list('id', 'title', 'slug')

    return {
        'pages': pages
    }