# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

# Изначальное решение
user_length = 5 #int(input('Enter the length of list: '))
list_my = list(range(1, user_length+1))
summ = 0
for i in list_my:
    list_my[i-1] = random.randint(1, 9)
    if not i % 2:
        summ += list_my[i-1]

print(f'{list_my} -> {summ}')



summ = 0
list_my = [random.randint(1,9) for i in range(user_length)]
list_my = list(enumerate(list_my))
for i, elem in list_my:
    if i % 2 == 1:
        summ += elem
print(f'{list_my} -> {summ}')
