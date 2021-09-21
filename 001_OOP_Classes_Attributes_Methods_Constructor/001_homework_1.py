# Создать класс, описывающий книгу. Содержащий информацию об авторе, названии, годе издания и  жанре.
# Создать несколько разных книг. Определить операции проверки на
# равенство и неравенство, методы __repr__ и __str__.


# Класс книг
class Book():
    # Метод конструктора
    def __init__(self, author, name, year, genre):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre

    # Метод представления объекта
    def __repr__(self):
        return f'Book name - {self.name}, author - {self.author}, published in {self.year}, genre - {self.genre}'

    # Метод представления объекта
    def __str__(self):
        return f'Book name: {self.name}, author: {self.author}, published in {self.year}, genre: {self.genre}'

    # Операция равенства
    def __eq__(self, other):
        return self.name == other.name and self.author == other.author and \
               self.year == other.year and self.genre == other.genre

    # Операция не равенства
    def __ne__(self, other):
            return not (self == other)


# Главная функция
def main():
    book1 = Book('Serge', 'First book', 2008, 'Horror')
    book2 = Book('Alex', 'Book 1999', 2008, 'Comedy')
    book3 = Book('Serge', 'First book', 2008, 'Horror')
    book4 = book1

    print('Methods __repr__ and __str__:')
    print(f'__repr__ - {book1.__repr__()}')
    print(f'__str__ - {book1.__str__()}')
    print()
    print('Book equality check:')
    print('book1 == book2 - ', book1 == book2)
    print('book1 == book3 - ', book1 == book3)
    print('book1 == book4 - ', book1 == book4)
    print()
    print('Checking the inequality of books:')
    print('book1 != book2 - ', book1 != book2)
    print('book1 != book3 - ', book1 != book3)
    print('book1 != book4 - ', book1 != book4)


# Начало программы
if __name__ == '__main__':
    main()