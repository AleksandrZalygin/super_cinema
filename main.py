import os
import requests

from film import Film
from film_pagination import FilmPagination
from user import User


URL_API = 'https://kinopoiskapiunofficial.tech/api/v2.2/films?'
API_KEY = '9d7b6fe1-49a0-4e72-b99e-7c385789bbca'
films = []
all_genres_of_films = []

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

        for genre in film.genres:
            if genre['genre'] != '' and genre['genre'] != None:
                if genre['genre'] not in all_genres_of_films:
                    all_genres_of_films.append(genre['genre'])

        films.append(film)

    page_number += 1

films = sorted(films, key=lambda film: film.rating, reverse=True)


print('Добро пожаловать в онлайн-кинотеатр "SuperCinema"!')
while True:
    user_name = input('Введите Ваш ник: ')
    if f"{user_name.replace('@', '')}.json" in os.listdir('data'):
        user = User(user_name, films)
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


choice = input('''Что хотите сделать?
1. Вывести топ фильмов.
2. Найти фильм по названию.
3. Найти фильмы по жанру.
4. Вывести просмотренные фильмы.
5. Вывести фильмы из "Смотреть позже".
> ''')

return_to_previous = False
if choice == '1':
    film_pagination = FilmPagination(films, 5)
    print('\nФильмы: ')
    while True:
        if return_to_previous:
            print(film_pagination.return_to_previous_films())
            return_to_previous = False
        else:
            print(next(film_pagination))

        print(f'\n...\nСтраница {film_pagination.current_page} из {len(films) // 5}\n')
        choice_of_next_page = input('''Хотите посетить следующую страницу?
1. Следующая.
2. Предыдущая.
3. Добавить фильм в "Просмотренные".
4. Добавить фильм в "Смотреть позже".
5. Выход.
> ''')
        if choice_of_next_page == '1':
            continue
        elif choice_of_next_page == '2':
            return_to_previous = True
            continue
        elif choice_of_next_page == '3':
            number_of_film_to_viewed = int(input(
'Какой фильм хотите добавить в "Просмотренные"?\nОт 1 до 5: '))
            user_grade = input('Ваша оценка фильму: ')
            if user.add_film_to_viewed(5 * film_pagination.current_page - (6 - number_of_film_to_viewed),
                                        user_grade):
                print('Успешно добавлено!')
        elif choice_of_next_page == '4':
            number_of_film_to_watch_later = int(input(
'Какой фильм хотите добавить в "Cмотреть позже"?\nОт 1 до 5: '))
            if user.add_film_to_watch_later(5 * film_pagination.current_page - (6 - number_of_film_to_watch_later)):
                print('Успешно добавлено!')
        else:
            break 
elif choice == '2':
    search_film_title = input('Введите название фильма: ')
    suitable_films = Film.search_films_by_title(films, search_film_title)

    if len(suitable_films) >= 5:
        film_pagination = FilmPagination(suitable_films, 5)
    else:
        film_pagination = FilmPagination(suitable_films, len(suitable_films))
        
    print('\nФильмы: ')
    while True:
        if return_to_previous:
            print(film_pagination.return_to_previous_films())
            return_to_previous = False
        else:
            print(next(film_pagination))

        if len(suitable_films) >= 5:
            print(f'\n...\nСтраница {film_pagination.current_page} из {len(suitable_films) // 5}\n')
        else:
            print(f'\n...\nСтраница {film_pagination.current_page} из {len(suitable_films) // len(suitable_films)}\n')
        choice_of_next_page = input('''Хотите посетить следующую страницу?
1. Следующая.
2. Предыдущая.
3. Добавить фильм в "Просмотренные".
4. Добавить фильм в "Смотреть позже".
5. Выход.
> ''')
        if choice_of_next_page == '1':
            continue
        elif choice_of_next_page == '2':
            return_to_previous = True
            continue
        elif choice_of_next_page == '3':
            number_of_film_to_viewed = int(input(
'Какой фильм хотите добавить в "Просмотренные"?\nОт 1 до 5: '))
            user_grade = input('Ваша оценка фильму: ')
            if user.add_film_to_viewed(5 * film_pagination.current_page - (6 - number_of_film_to_viewed),
                                        suitable_films,
                                        user_grade):
                print('Успешно добавлено!')
        elif choice_of_next_page == '4':
            number_of_film_to_watch_later = int(input(
'Какой фильм хотите добавить в "Cмотреть позже"?\nОт 1 до 5: '))
            if user.add_film_to_watch_later(5 * film_pagination.current_page - (6 - number_of_film_to_watch_later),
                                            suitable_films):
                print('Успешно добавлено!')
        else:
            break 
elif choice == '3':
    print('\nВсе жанры: ')
    for index, genre in enumerate(all_genres_of_films, 1):
        print(f'{index}. {genre}')

    search_film_genre = input('\nВведите жанр: ')
    suitable_films = Film.search_films_by_genre(films, search_film_genre)
    if len(suitable_films) >= 5:
        film_pagination = FilmPagination(suitable_films, 5)
    else:
        film_pagination = FilmPagination(suitable_films, len(suitable_films))
    print('\nФильмы: ')
    while True:
        if return_to_previous:
            print(film_pagination.return_to_previous_films())
            return_to_previous = False
        else:
            print(next(film_pagination))

        if len(suitable_films) >= 5:
            print(f'\n...\nСтраница {film_pagination.current_page} из {len(suitable_films) // 5}\n')
        else:
            print(f'\n...\nСтраница {film_pagination.current_page} из {len(suitable_films)}\n')

        choice_of_next_page = input('''Хотите посетить следующую страницу?
1. Следующая.
2. Предыдущая.
3. Добавить фильм в "Просмотренные".
4. Добавить фильм в "Смотреть позже".
5. Выход.
> ''')
        if choice_of_next_page == '1':
            continue
        elif choice_of_next_page == '2':
            return_to_previous = True
            continue
        elif choice_of_next_page == '3':
            number_of_film_to_viewed = int(input(
'Какой фильм хотите добавить в "Просмотренные"?\nОт 1 до 5: '))
            user_grade = input('Ваша оценка фильму: ')
            if user.add_film_to_viewed(5 * film_pagination.current_page - (6 - number_of_film_to_viewed),
                                        suitable_films,
                                        user_grade):
                print('Успешно добавлено!')
        elif choice_of_next_page == '4':
            number_of_film_to_watch_later = int(input(
'Какой фильм хотите добавить в "Cмотреть позже"?\nОт 1 до 5: '))
            if user.add_film_to_watch_later(5 * film_pagination.current_page - (6 - number_of_film_to_watch_later),
                                            suitable_films):
                print('Успешно добавлено!')
        else:
            break
elif choice == '4':
    while True:
        choice_of_sort_films = input('''\nКакой метод сортировки фильмов выберете?
1. По рейтингу: от лучшего к худшему.
2. По рейтингу: от худшего к лучшему.
3. Определённого жанра.
> ''')
        if choice_of_sort_films == '1':
            viewed_films = user.get_user_films_from_json_viewed(True)

            for index, film in enumerate(viewed_films.keys(), 1):
                print(f'{index}. {film}. Ваша оценка: {viewed_films[film]}')
            break
        elif choice_of_sort_films == '2':
            viewed_films = user.get_user_films_from_json_viewed()

            for index, film in enumerate(viewed_films.keys(), 1):
                print(f'{index}. {film}. Ваша оценка: {viewed_films[film]}')
            break
        elif choice_of_sort_films == '3':
            search_film_genre = input('\nВведите жанр: ')
            viewed_films = user.get_user_films_from_json_viewed_with_genre(search_film_genre)

            for index, film in enumerate(viewed_films, 1):
                print(f'{index}. {film}. Ваша оценка: {viewed_films[film]}')
            break
        else:
            print('Ошибка! Введите число от 1 до 3!')
            continue
elif choice == '5':
    watch_later_films = user.get_user_films_from_json_watch_later()

    for index, film in enumerate(watch_later_films, 1):
        print(f'{index}. {film}')
else:
    print('Ошибка! Введите число от 1 до 5!')
