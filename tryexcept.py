# Задание 1
#Напишите программу, которая запрашивает у пользователя число и обрабатывает ошибку, если введено не число.
while True:
    try:
        number = float(input("Введите число: "))
        print("Вы ввели число: ", number)
        break
    except ValueError:
        print("Ошибка! Это не число. Попробуйте снова")

# Задание 2
# Напишите программу, которая пытается открыть файл и обрабатывает ошибку, если файл не существует
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print("Содержимое файла: ")
        print(content)
except FileNotFoundError:
    print("Ошибка: Файл 'example.txt' не найден")