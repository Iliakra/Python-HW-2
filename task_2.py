""" Красильников Илья
1. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2
и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input().
"""

input_values = input("Введите элементы списка через запятую  ")
my_list = input_values.split(",")
print(my_list)

for item in my_list:
    item_index = my_list.index(item)
    if item_index % 2 != 0:
        prev_item_value = my_list[item_index-1]
        prev_item_index = item_index-1
        my_list[prev_item_index] = item
        my_list[item_index] = prev_item_value

print(my_list)
