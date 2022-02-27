import json
import os

from exceptions import FileAlreadyExist, NotCorrectNickName, NotCorrectPassword

class User:
    def __init__(self, user_name: str):
        self.user_name = user_name

    def registration_new_user(self, password):
        if f"{self.user_name.replace('@', '')}.json" in os.listdir('data'):
            raise FileAlreadyExist('Такой пользователь уже существует!')
            return False

        for letter in self.user_name:
            if not self.user_name.startswith('@') or letter in r'[0-9]':
                raise NotCorrectNickName('Некорректное имя пользователя!')
                return False

        if len(password) < 8:
            raise NotCorrectPassword('Пароль не может быть меньше восьми символов!')
            return False

        self.__create_json_file(password)
        return True

    def __create_json_file(self, password):
        user_data = {
            "nickname": self.user_name,
            "password": password,
            "statistic": {}
        }

        with open(f'data/{self.user_name.replace("@", "")}.json', 'w', encoding='utf-8') as json_file:
            json.dump(user_data, json_file, ensure_ascii=False)
        return True

    def get_right_password_from_json(self):
        with open(f'data/{self.user_name.replace("@", "")}.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data['password']

    def add_film_to_viewed(self, film, grade):
        with open(f'data/{self.user_name.replace("@", "")}.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        data['Просмотренные'][film.name] = {
                                        "film_obj": film,
                                        "genres": film.genres,
                                        "grade": grade
                                    }

        with open(f'data/{self.user_name.replace("@", "")}.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)

    def add_film_to_watch_later(self, film):
        with open(f'data/{self.user_name.replace("@", "")}.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        data['Смотреть позже'][film.name] = {
                                        "film_obj": film,
                                        "genres": film.genres,
                                        "grade": film.rating
                                    }

        with open(f'data/{self.user_name.replace("@", "")}.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)
