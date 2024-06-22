import requests

def get_movie_poster(api_key, movie_title):
    # Endpoint de búsqueda de películas
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}"
    search_response = requests.get(search_url)
    search_data = search_response.json()

    if search_data['results']:
        # Obtener el ID de la primera película encontrada
        movie_id = search_data['results'][0]['id']

        # Endpoint de detalles de la película
        details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
        details_response = requests.get(details_url)
        details_data = details_response.json()

        # Obtener la ruta del póster
        poster_path = details_data.get('poster_path')
        if poster_path:
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
            return poster_url
        else:
            return "No se encontró póster para esta película."
    else:
        return "No se encontraron resultados para esta búsqueda."