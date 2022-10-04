import os
from enum import Enum

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')  # Назначили ссылку на метод в поле clear

class Action(Enum):
    exit = '0'
    add_book = '1'
    list_book = '2'
    info_book = '3'
    del_book = '4'


class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.set_year(year)
        self.__author = author

    def __str__(self):
        return f'{self.title}, год издания - {self.__year}, автор - {self.__author}'

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        assert type(title) is str, "не строка"
        self.__title = title

    def set_year(self, year):
        if isinstance(year, int):
            self.__year = year


class Library:
    books = []

    def add(self, book):
        self.books.append(book)
        print(f'Книга под номером {len(self.books)} добавлена')

    def removeAt(self, book):
        if 0 < book <= len(self.books):
            self.books.pop(book - 1)
            return 'книга удалена'
        else:
            return "книги с таким номером нет"

    def printAll(self):
        for num, item in enumerate(self.books, 1):
            d = str(item).split(',')
            print(f"{num} - {d[0]}")

    def printAt(self, book):
        if 0 < book <= len(self.books):
            print(f'{book} - {self.books[book - 1]}')
        else:
            print("книги с таким номером нет")


if __name__ == '__main__':
    select = None
    lib = Library()
    books = [('Автоматизация рутинных задач с помощью python 2-е издание', 2021, 'Эл Свейгарт'), ('Создаём программы и игры 2-е издание', 2019, 'Кольцов Д. В.')]
    for book in books:
        b = Book(*book)
        lib.add(b)
    while select != '0':
        print(f'''Введите номер?
        {Action.exit.value} - Выйти
        {Action.add_book.value} - Добавить книгу
        {Action.list_book.value} - Посмотреть список
        {Action.info_book.value} - Информация о книге
        {Action.del_book.value} - Удалить книгу''')
        select = input(">>: ")

        clear()  # Вызываем при необходимости очистки консоли

        # exit
        if select == Action.exit.value:
            print('Пока.')
        # добавить
        elif select == Action.add_book.value:
            title = input('название: ')
            while True:
                year = input('год: ')
                if year.isdigit():
                    year = int(year)
                    break
                else:
                    print('Введите число')
            author = input('автор: ')
            b = Book(title, year, author)
            lib.add(b)
        # список
        elif select == Action.list_book.value:
            lib.printAll()
        # Информация о книге
        elif select == Action.info_book.value:
            num_book = input('Введите номер книги: ')
            if num_book.isdigit():
                num_book = int(num_book)
                lib.printAt(num_book)
            else:
                print('это не цифра')
        # удалить
        elif select == Action.del_book.value:
            num_book = input('Введите номер книги которую хотите удалить: ')
            if num_book.isdigit():
                num_book = int(num_book)
                print(lib.removeAt(num_book))
            else:
                print('это не цифра')
        # неправильный ввод
        else:
            print('\nНеправильный ввод!')
