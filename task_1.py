#  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
num_1 = input("Введите вещественное число: ")
sum_1 = sum(map(int, num_1.replace(',', '')))
print (f' Сумма цифр числа {num_1} равна: {sum_1}')

