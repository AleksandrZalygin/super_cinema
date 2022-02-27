class Film:
    @staticmethod
    def search_films_by_title(films, user_title):
        films = sorted(films, key=lambda film: film.year)
        for film in films:
            if user_title in film.title:
                yield f'{film.title} ({film.year}), {film.rating}\n'

    @staticmethod
    def search_films_by_genre(films, user_genre):
        for film in films:
            if user_genre in [genre['genre'] for genre in film.genres]:
                yield f'{film.title} ({film.year}), {film.rating}\n'


    def __init__(self, film_hash):
        self.title = film_hash["nameRu"]
        self.year = film_hash["year"]
        self.genres = film_hash["genres"]
        self.rating = film_hash["ratingKinopoisk"]

    def __str__(self):
        return f"Название: {self.title}. Год {self.year}. Жанры {', '.join([str(genre['genre']) for genre in self.genres])}. Рейтинг {self.rating}."

    def __iter__(self):
        return self
    
    def __next__(iterable):
        return f'{next(iterable)}\n{next(iterable)}\n{next(iterable)}\n{next(iterable)}\n{next(iterable)}\n'

""" def for_loop(iterable, loop_body_function):
    iterator = iter(iterable)
    next_element_exist = True
    while next_element_exist:
        try:
            element_from_iterator = next(iterator)
        except StopIteration:
            next_element_exist = False
        else:
            loop_body_function(element_from_iterator)

for_loop([0, 1, 2, 3], print) """