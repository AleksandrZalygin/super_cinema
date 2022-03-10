class Film:
    @staticmethod
    def search_films_by_title(films: list, user_title: str):
        suitable_films = []
        films = sorted(films, key=lambda film: film.year)
        for film in films:
            if user_title in film.title:
                suitable_films.append(film)
        return suitable_films
                # yield f'{film.title} ({film.year}), {film.rating}\n'

    @staticmethod
    def search_films_by_genre(films: list, user_genre: str):
        suitable_films = []
        for film in films:
            if user_genre in [genre['genre'] for genre in film.genres]:
                suitable_films.append(film)
        return suitable_films


    def __init__(self, film_hash: object):
        self.title = film_hash["nameRu"]
        self.year = film_hash["year"]
        self.genres = film_hash["genres"]
        self.rating = film_hash["ratingKinopoisk"]

    def __str__(self):
        return f"{self.title} ({self.year}) Рейтинг: {self.rating}"
        # Жанры: ', '.join([str(genre['genre']) for genre in self.genres])
