# Задание 1
# Напишите программу, которая запрашивает у пользователя два числа и выводит их сумму.
num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
sum = num_1 + num_2
print(sum)


# Задание 2
# Напишите программу, которая преобразует введенное пользователем число из строки в целое число и выводит его тип данных.
num = input("Введите число: ")
num_int = int(num)
print("Число: ", num_int)
print("Тип данных: ", type(num_int))

#Задание 3
#Напишите программу, которая запрашивает у пользователя его возраст и выводит сообщение: "Вам [возраст] лет."
age = int(input("Введите свой возраст: "))
print(f"Вам {age} лет.")