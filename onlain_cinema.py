class OnlainCinema:
    def search_films_by_title(films: list, user_title: str):
        suitable_films = []
        films = sorted(films, key=lambda film: film.year)
        for film in films:
            if user_title in film.title:
                suitable_films.append(film)
        return suitable_films

    def search_films_by_genre(films: list, user_genre: str):
        suitable_films = []
        for film in films:
            if user_genre in [genre['genre'] for genre in film.genres]:
                suitable_films.append(film)
        return suitable_films
