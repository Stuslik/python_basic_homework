# Создать класс Tiger, унаследованный от класса Cat (созданного во время практической части занятия).
# Переопределить метод set_size таким образом, чтобы если self.cat_type это ‘wild’, то self.size
# = ‘big’, иначе self.size=’undefined’


# Класс кота
class Cat:
    # Метод конструктора
    def __init__(self, color, cat_type, size="undefined"):
        self.size = size
        self.color = color
        self.cat_type = cat_type

    # Метод размера
    def set_size(self):
        if self.cat_type == "indoor":
            self.size = "small"
        elif self.cat_type == "wild":
            self.size = "big"
        else:
            self.size = "undefined"


# Класс тигра
class Tiger(Cat):
    # Переопределение метода размера
    def set_size(self):
        if self.cat_type == 'wild':
            self.size = 'big'
        else:
            self.size = 'undefined'


# Главная функция
def main():
    anna = Tiger('white', 'indoor')
    anna.set_size()
    print(f'Tiger Anna ({anna.color}) size: {anna.size}')

    boris = Tiger('black', 'wild')
    boris.set_size()
    print(f'Tiger Boris ({boris.color}) size: {boris.size}')


# Начало программы
if __name__ == '__main__':
    main()
