# Задание 1
# Напишите программу, которая выводит все числа от 1 до 10 с использованием цикла for
for i in range(1, 11):
    print(i)

#Задание 2
# Напишите программу, которая выводит все числа от 1 до N, где N вводит пользователь
n = int(input("Введите количество чисел: "))
for i in range (1, n+1):
    print(i)

# Задание 3 
# Напишите программу, которая вычисляет сумму всех чисел от 1 до 100 с использованием цикла while
sum = 0
current_num = 1
while current_num <= 100:
    sum += current_num
    current_num += 1
print("Сумма чисел от 1 до 100: ", sum)