class Film:
    def __init__(self, film_hash: object):
        self.title = film_hash["nameRu"]
        self.year = film_hash["year"]
        self.genres = film_hash["genres"]
        self.rating = film_hash["ratingKinopoisk"]

    def __str__(self):
        return f"{self.title} ({self.year}) Рейтинг: {self.rating}"
        # Жанры: ', '.join([str(genre['genre']) for genre in self.genres])
