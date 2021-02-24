import requests
import base64
import json

def get_films(name_film):
    """
        Función que se encarga de obtener las caracteristicas
        de la película seleccionada a través de la llamada 
        a la api SWAPI

    Args:
        name_film (String): Nombre de la película.

    Returns:
        [list]: Contiene una lista con un diccionario
                con las características de la película
                seleccionada.
    """

    films = []
    for i in range(1,7):
        film = requests.get("https://swapi.dev/api/films/"+str(i)+"/")
        data_film = json.loads(film.text)
        if data_film['title'] == name_film:
            films.append(data_film)
            break
        
    return films


