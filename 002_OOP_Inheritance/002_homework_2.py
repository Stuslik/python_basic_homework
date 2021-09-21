# Создать иерархию классов с использованием множественного наследования. Вывести на экран
# порядок разрешения методов для каждого из классов. Объяснить, почему линеаризации данных
# классов выглядят именно так.


# Телефон
class Telephone():
    def call(self):
        pass


# Здание
class Building():
    def adress(self):
        pass


# Телефонная будка
class Phone_Booth(Telephone, Building):
    def money(self):
        pass


# Главная функция
def main():
    print(Building.__mro__)
    print(Telephone.__mro__)
    print(Phone_Booth.__mro__)


# Начало программы
if __name__ == '__main__':
    main()