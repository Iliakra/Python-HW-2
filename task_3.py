""" Красильников Илья
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""

month_number = int(input("Введите месяц в виде целого числа  "))

# -------LIST-------
month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for item in month_list:
    if month_number == item:
        if item < 3 or item == 12:
            print("Это зима")
            break
        elif 6 > item > 2:
            print("Это весна")
            break
        elif 9 > item > 5:
            print("Это лето")
            break
        else:
            print("Это осень")
            break

# -------DICT-------
month_dict = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}

for key, value in month_dict.items():
    for item in value:
        if item == month_number:
            print(f"Это {key}")
            break
