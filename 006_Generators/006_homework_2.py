# Вывести из списка чисел список квадратов четных чисел. Используйте 2 варианта решения: генератор и цикл


my_list = [1, 3, 6, 10, 5, -4]
print(f'Original my_list: {my_list}\n')

# Через цикл for
list_res = []
for num in my_list:
    if num % 2 == 0:
        list_res.append(num ** 2)
print(f'Squared even numbers (used a for loop): {list_res}')

# Через генератор
def parity():
    for num in my_list:
        if num % 2 == 0:
            list_res.append(num ** 2)
            yield


list_res = []
generator = parity()
while True:
    try:
        next(generator)
    except StopIteration:
        break

print(f'Squared even numbers (used a generator): {list_res}')
