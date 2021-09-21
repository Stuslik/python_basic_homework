# Создать класс, описывающий отзыв к книге. Добавить в класс книги поле – список отзывов.
# Сделать так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.


# Класс книг
class Book():
    # Метод конструктора
    def __init__(self, author, name, review):
        self.author = author
        self.name = name
        self.review = review

    # Метод представления объекта
    def __str__(self):
        return f'Book name: {self.name}, author: {self.author}, review: {self.review}'


# Класс отзывов
class Review():
    # Метод конструктора
    def __init__(self, rew_author, rew_review):
        self.rew_author = rew_author
        self.rew_review = rew_review

    # Метод представления объекта
    def __str__(self):
        return f'Review author: {self.rew_author}, text review: {self.rew_review}'


# Главная функция
def main():
    review1 = Review('Trol', 'Bad book')
    book1 = Book('Serge', 'First book', review1)
    review2 = Review('Anna', 'Nice fantasy')
    book2 = Book('Alex', 'Book 1999', review2)

    print(f'{book1}')
    print(f'{book2}')


# Начало программы
if __name__ == '__main__':
    main()
