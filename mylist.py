# Задание 1
# Напишите программу, которая создает список из 5 чисел и выводит их сумму
list = []
for i in range(5):
    num = int(input("Введите число: "))
    list.append(num)
print(sum(list))

# Задание 2
# Напишите программу, которая находит максимальное число в списке
list_max = []
n = int(input("Введите количество чисел в списке: "))
for i in range(n):
    num_max = int(input("Введите число: "))
    list_max.append(num_max)
print(max(list_max))

# Задание 3
# Напишите программу, которая удаляет дубликаты из списка
list_orig = []
list_unique = []
N = int(input("Введите количество чисел в списке: "))
for i in range(N):
    number = int(input("Введите числа: "))
    list_orig.append(number)

for item in list_orig:
    if item not in list_unique:
        list_unique.append(item)
print("Список без дубликатов: ", list_unique)