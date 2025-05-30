# Задание 1
# Напишите программу, которая генерирует случайное число от 1 до 100 с использованием модуля random
import random
random_number = random.randint(1, 100)
print("Случайное число от 1 до 100: ", random_number)

# Задание 2
# Напишите программу, которая выводит текущую дату и время с использованием модуля datetime
import datetime
now = datetime.datetime.now()
formatted_now = now.strftime("%d-%m-%Y %H:%M:%S")
print("Текущая дата и время: ", formatted_now)

# Задание 3
# Напишите программу, которая вычисляет квадратный корень числа с использованием модуля math рядом напишите программу которая вычесляет квадратный корень без модуля math
import math
number = float(input("Введите число: "))
if number < 0:
    print("Ошибка: не можем найти квадратный корень из отрицательного числа")
else:
    sqrt = math.sqrt(number)
    print(f"Квадратный корень из {number} равен {sqrt}")


num = float(input("Введите число: "))
print("Квадратный корень:", num ** 0.5)