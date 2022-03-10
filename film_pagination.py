class FilmPagination:
    def __init__(self, films: list, count_iters: int):
        self.films = films
        self.count_iters = count_iters
        self.cursor = -1
        self.current_page = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current_page += 1

        string_for_return = ''
        loop = 0
        while loop < self.count_iters:
            loop += 1
            self.cursor += 1

            if self.cursor >= len(self.films):
                raise StopIteration()
                
            string_for_return += f'\n\n{loop}. {self.films[self.cursor]}'
        return string_for_return

    def return_to_previous_films(self):
        self.cursor -= 10
        self.current_page -= 2
        return self.__next__()
