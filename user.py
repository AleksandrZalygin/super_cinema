import json
import os
from itertools import product

from exceptions import FileAlreadyExist, NotCorrectNickName, NotCorrectPassword

class User:
    @staticmethod
    def registration_new_user(self, password: str):
        if f"{self.user_name.replace('@', '')}.json" in os.listdir('data'):
            raise FileAlreadyExist('Такой пользователь уже существует!')

        for letter in self.user_name:
            if not self.user_name.startswith('@') or letter in r'[0-9]':
                raise NotCorrectNickName('Некорректное имя пользователя!')

        if len(password) < 8:
            raise NotCorrectPassword('Пароль не может быть меньше восьми символов!')

        self._create_json_file(password)
        return True


    def __init__(self, user_name: str, films: list):
        self.user_name = user_name
        self.films = films

    def _create_json_file(self, password: str):
        user_data = {
            "nickname": self.user_name,
            "password": password,
            "Просмотренные": {},
            "Смотреть позже": {}
        }

        with open(f'data/{self.user_name.replace("@", "")}.json', 'w', encoding='utf-8') as json_file:
            json.dump(user_data, json_file, ensure_ascii=False)
        return True

    def get_right_password_from_json(self):
        with open(f'data/{self.user_name.replace("@", "")}.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data['password']

    def add_film_to_viewed(self, index_of_film: int, films: str, user_grade: str):
        with open(f'data/{self.user_name.replace("@", "")}.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        film = films[index_of_film]
        data['Просмотренные'][film.title] = {
                                        "genres": ', '.join([str(genre['genre']) for genre in film.genres]),
                                        "user_grade": user_grade
                                    }


        with open(f'data/{self.user_name.replace("@", "")}.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)
            
        return True

    def add_film_to_watch_later(self, index_of_film: int, films: str):
        with open(f'data/{self.user_name.replace("@", "")}.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        film = films[index_of_film]
        data['Смотреть позже'][film.title] = {
                                        "genres": ', '.join([str(genre['genre']) for genre in film.genres]),
                                        "grade": film.rating
                                    }

        with open(f'data/{self.user_name.replace("@", "")}.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)

        return True

    def get_user_films_from_json_viewed(self, reverse=False):
        with open(f'data/{self.user_name.replace("@", "")}.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        films_to_return = {}
        map(lambda film: films_to_return.update({film: float(data['Просмотренные'][film.title]['user_grade'])}),
            [film for film_title, film in product(data['Просмотренные'].keys(), self.films) if film.title == film_title])


        ''' for film_title in data['Просмотренные']:
            for film in self.films:
                if film_title == film.title:
                    films_to_return[film] = float(data['Просмотренные'][film_title]['user_grade']) '''

        sorted_films_by_rating = sorted(films_to_return.values(), reverse=reverse)
        sorted_films = {}

        for grade in sorted_films_by_rating:
            for film_name in films_to_return.keys():
                if films_to_return[film_name] == grade:
                    sorted_films[film_name] = films_to_return[film_name]
                    break
        return sorted_films

    def get_user_films_from_json_viewed_with_genre(self, user_genre):
        with open(f'data/{self.user_name.replace("@", "")}.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        films_to_return = []
        for film_title, film in product(data['Просмотренные'], self.films):
            if film_title == film.title:
                films_to_return.append(film)

        # films_to_return = [film for film_title, film in product(data['Просмотренные'], self.films) if film_title == film.title]
        
        suitable_films = {}
        for film in films_to_return:
            if user_genre in [genre['genre'] for genre in film.genres]:
                suitable_films[film] = float(data['Просмотренные'][film_title]['user_grade'])
        return suitable_films

    def get_user_films_from_json_watch_later(self):
        with open(f'data/{self.user_name.replace("@", "")}.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        films_to_return = []
        for film_title, film in product(data['Смотреть позже'], self.films):
            if film_title == film.title:
                films_to_return.append(film)

        return films_to_return
