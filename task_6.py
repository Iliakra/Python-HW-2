""" Красильников Илья
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя.
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
"""
product_list = [0]

for index, el in enumerate(product_list):
    product_title = input("Введите название товара   ")
    product_price = input("Введите стоимость товара   ")
    product_amount = input("Введите количество товара   ")
    amount_unit = input("Введите единицы измерения количества товара   ")
    el = (index + 1, {"название": product_title, "цена": product_price, "количество": product_amount, "ед.": amount_unit})
    product_list[index] = el
    continue_inserting = input("Ввести еще один товар? Напишите Да или Нет   ")
    if continue_inserting == "Да":
        product_list.append(1)

print(product_list)

result_dict = {}
attributes_keys = []

for item in product_list:
    product_attributes = item[1].keys()
    attributes_keys.extend(product_attributes)
result_dict_keys = list(set(attributes_keys))

for item in result_dict_keys:
    result_list = []
    for el in product_list:
        attributes_dict = el[1]
        for key, value in attributes_dict.items():
            if key == item:
                result_list.append(value)
    if item == "ед.":
        result_list = list(set(result_list))
    result_dict.update({item: result_list})

print(result_dict)




