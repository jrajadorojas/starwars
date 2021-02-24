# Django
from django.shortcuts import render, get_object_or_404

# Models
from app.models import Film

# Utilities
from app.utils import get_films

# Lists encargadas de ir guardando las urls.
view_index = []
detail = []
search = []


def index(request):
    """
        Función principal de la aplicación.
        Es la encargada de visualizar la página
        inicial de la aplicación (Navbar, Carousel
        y listado de películas.).
        Se obtiene a través del ORM todas las películas.
        En este caso, solamente contiene 6.
    Args:
        request: Petición inicial de la aplicación

    Returns:
        Template: Se visualiza index.html.
    """

    view_index.append(request.get_full_path())
    films = Film.objects.all()
    
    context = {
        'films': films,
    }
    return render(request, 'app/index.html', context)


def film_detail(request, slug):
    """
        Función encargada de visualizar un detalle
        de la película que el usuario haya pulsado.
        Para ello obtenemos el valore del slug para 
        obtener la imágen y el título.
        Obtenemos el nombre de la película para recu
        perar a través de la llamada get_films todos
        los datos referente a la película seleccionada

    Args:
        request: Petición para visualizar el detalle
                 de una película.
        slug (String): Slug de una película

    Returns:
        Template: Se visualiza detail.html
    """

    detail.append(request.get_full_path())
    film = get_object_or_404(Film,slug=slug)
    data_films = get_films(film.name)
    context = {
        'film': film,
        'description': data_films[0]['opening_crawl'],
    }
    return render(request, 'app/detail.html', context)


def search_films(request):
    """
        El usuario a través del input situado en el Navbar
        del template principal, puede buscar una película
        que esté almacenada en el sistema.

    Args:
        request: Petición de búsqueda de una película.

    Returns:
        Template: Se visuualiza detail.html
    """

    search.append(request.get_full_path())
    
    search_film = request.GET['film']
    film = Film.objects.filter(name__contains=search_film).values('name','slug','image')
    data_films = get_films(film[0]['name'])
    
    context = {
        'search': True,
        'film': film[0]['name'],
        'image': '/media/'+film[0]['image'],
        'description': data_films[0]['opening_crawl'],
    }
    return render(request, 'app/detail.html', context)


def path_views(request):
    """
        Cuando el usuario esté nevegando por cada una
        de las pantallas de la aplicación, se irán
        guardando las url para después mostrarlas.

    Args:
        request: Petición para visualizar los path visitados.

    Returns:
        Template: Se visualiza path_views.html
    """


    context = {
        'view_index': view_index,
        'detail':detail,
        'search': search,
    }
    return render(request, 'app/path_views.html', context)
