# Написать генератор, который возвращает элементы заданного списка в обратном порядке (аналог reversed).


my_list = [1, 3, 6, 10]
print(f'Original my_list: {my_list}')

generator = [x for x in my_list[::-1]]
print(f'Reversed my_list: {generator}')
