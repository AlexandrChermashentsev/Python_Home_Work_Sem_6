# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# Мое старое решение
def summ_numbers(x):
    summ = 0
    while x % 10 != 0:
        summ = summ + x % 10
        x //= 10
    return summ

user_number = input('Enter the float number: ')
print_user_number = user_number
if not '.' in user_number:
    user_number = int(user_number)
    print(summ_numbers(user_number))
else:
    user_number = user_number.replace('.', '')
    user_number = int(user_number)
    print(f'{print_user_number} -> {summ_numbers(user_number)}')
            

# Новое решение
nmbr = input("Введите вещественное число: ")
lst = [int(i) for i in nmbr if i.isdigit()]
summ = sum(lst)
print(summ)