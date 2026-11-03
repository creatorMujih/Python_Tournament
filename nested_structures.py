movies = [
    {"id": 1, "title": "Inception", "year": 2010, "genre": "Sci-Fi"},
    {"id": 2, "title": "Titanic", "year": 1997, "genre": "Romance"},
    {"id": 3, "title": "Avatar", "year": 2009, "genre": "Action"}
]

def search_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    return "Movie not found"


def add_movie(movie):
    for existing_movie in movies:
        if existing_movie["id"] == movie["id"]:
            return "Error: Duplicate movie ID!"

    movies.append(movie)
    return "Movie added successfully!"


print(search_movie(2))

new_movie = {
    "id": 4,
    "title": "Interstellar",
    "year": 2014,
    "genre": "Sci-Fi"
}

print(add_movie(new_movie))

duplicate_movie = {
    "id": 2,
    "title": "The Matrix",
    "year": 1999,
    "genre": "Sci-Fi"
}

print(add_movie(duplicate_movie))
