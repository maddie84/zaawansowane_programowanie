import json

class Movie:
    def __init__(self, movield, title, genres):
        self.movield = movield
        self.title = title
        self.genres = genres

def load_movies_from_file(file_path):
    movies = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            values = line.strip().split(',')
            movield = values[0]
            title = values[1]
            genres = ','.join(values[2:])  
            movie = Movie(movield, title, genres)
            movies.append(movie.__dict__)
    return movies


def get_movies():
    file_path = 'movies.csv' 
    movies = load_movies_from_file(file_path)
    formatted_movies = []

    for movie in movies:
        formatted_movie = {
            "id": movie.movieId,
            "title": movie.title,
            "genres": movie.genres
        }
        formatted_movies.append(formatted_movie)

    return formatted_movies

# Przykładowe użycie
if __name__ == "__main__":
    movies = get_movies()
    for movie in movies:
        print(json.dumps(movie, indent=4))
