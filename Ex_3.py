# 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
import os
os.system('clear')


# Старое решение
def find_min_and_max_in_list(list): # Функция нахождения мин и макс в списке
    min, max = list[0], list[0] 
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
        elif list[i] > max:
            max = list[i]
    return min, max

def fractional_list(list_float): # Функция создания списка дробных частей вещественного списка
    fract_list = [] 
    for i in range(len(list_float)):
        fract_list.append(round(list_my[i] % 1, 2))
    return fract_list

list_my = [] # Блок инициализации списка
for i in range(5):
    list_my.append(round(random.uniform(0, 10), 2)) # рандом вещественных чисел

fract_list = fractional_list(list_my)
min1, max1 = find_min_and_max_in_list(fract_list)
print(f'{list_my} => {round(max1 - min1, 2)}')
print()

# Новое решение
def calc2(op, a, b):
    return op(a, b)

list_my = [round(random.uniform(0, 10), 2) for i in range(5)]
print(list_my)
list_my = [round(calc2(lambda i, y: i % y, i, 1), 2) for i in list_my]

print(f'{list_my} => {round(max(list_my) - min(list_my), 2)}')