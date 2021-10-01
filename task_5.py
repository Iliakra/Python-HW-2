""" Красильников Илья
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый
элемент с тем же значением должен разместиться после них.
"""

my_list = [7, 5, 3, 3, 2]
user_number = int(input("Введите целое натуральное число  "))
inserted = False
for index, value in enumerate(my_list):
    if user_number > value:
        my_list.insert(index, user_number)
        inserted = True
        break
    elif user_number == value:
        position = index + my_list.count(value)
        my_list.insert(position, user_number)
        inserted = True
        break

if not inserted:
    my_list.append(user_number)

print(my_list)


