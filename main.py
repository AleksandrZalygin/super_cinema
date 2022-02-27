import os
import requests

from film import Film
from user import User


URL_API = 'https://kinopoiskapiunofficial.tech/api/v2.2/films?'
API_KEY = '9d7b6fe1-49a0-4e72-b99e-7c385789bbca'
films = []

page_number = 1
while page_number < 21:
    response = requests.get(
        URL_API,
        params = {"page": page_number},
        headers = {
            "Content-type": "application/json",
            "X-API-KEY": API_KEY
        }
    ).json()

    for film_hash in response["items"]:
        film = Film(film_hash)

        if film.title == None:
            continue

        if film.title in [film.title for film in films]:
            continue

        films.append(film)

    page_number += 1

films = sorted(films, key=lambda film: film.rating, reverse=True)


print('Добро пожаловать в онлайн-кинотеатр "SuperCinema"!')
while True:
    user_name = input('Введите Ваш ник: ')
    if f"{user_name.replace('@', '')}.json" in os.listdir('data'):
        user = User(user_name)
        password = input('Введите пароль: ')
        if password == user.get_right_password_from_json():
            print('Авторизация прошла успешно.')
            break
        else:
            print('Ошибка! Пароль не верный!')
            continue
    else:
        print('Регистрация.')
        password = input('Введите пароль: ')
        user = User(user_name)
        if user.registration_new_user(password): 
            print('Регистрация прошла успешно!')
            break

""" choice = input('''Что хотите сделать?\n
1. Вывести топ фильмов.\n
2. Найти фильм по названию.\n
3. Найти фильмы по жанру.\n> 
''')

if choice == '1':
    while True:
        print(Film.__next__(films))
        choice_2 = input('Хотите посетить следующую страницу?\n1. Следующая.\n2. Выход.\n> ')
        if choice_2 == '1':
            continue
        else:
            break """

generator = Film.search_films_by_genre(films, 'драма')
print(Film.__next__(generator))
print(Film.__next__(generator))
