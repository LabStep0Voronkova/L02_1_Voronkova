# Задание 1
# Напишите функцию, которая принимает два числа и возвращает их сумму.
def sum_two_numbers(a, b):
    return a + b
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
res = sum_two_numbers(a, b)
print("Сумма: ", res)

# Задание 2
# Напишите функцию, которая проверяет, является ли число простым
def prime_number(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
num = int(input("Введите число: "))
print(prime_number(num))

# Задание 3
# Напишите функцию, которая принимает список чисел и возвращает их среднее значение
def average (numbers):
    return sum(numbers) / len(numbers)
nums = []
Nn = int(input("Введите количество чисел в списке: "))
for i in  range(Nn):
    num_list = int(input("Введите числа: "))
    nums.append(num_list)
print("Среднее значение: ", average(nums))