# Задание 1
# Напишите программу, которая создает текстовый файл и записывает в него строку "Hello, File!"
with open('hello.txt', 'w') as file:
    file.write("Hello, File!")
print("Строка записана в файл 'hello.txt'")

# Задание 2
# Напишите программу, которая читает содержимое файла и выводит его на экран
with open('hello.txt', 'r') as file:
    content = file.read()
    print("Содержание файла: ")
    print(content)

# Задание 3
# Напишите программу, которая добавляет новую строку в существующий файл
with open('hello.txt', 'a') as file:
    file.write("\nThis is a new line\n")
print("Новая строка добавлена в файл")