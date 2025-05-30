import random 
secret_number = random.randint(0, 10)
print("Добро пожаловать в игру 'Угадай число'!")
print("Я загадал число от 0 до 10. У тебя есть 3 попытки.")

attempts = 3

for attempt in range(attempts):
    try:
        guess = int(input(f"\nПопытка {attempt + 1}. Введите ваше число: "))
        if guess < 0 or guess > 10:
            print("Число должно быть в диапазоне от 0 до 10.")
            continue
        if guess == secret_number:
            print(f"Поздравляем! Вы угадали число {secret_number}!")
            break
        elif guess < secret_number:
            print("Не верно! Загаданное число больше!")
        else:
            print("Не верно! Загаданное число меньше!")
    except ValueError:
        print("Пожалуйста, введите целое число.")
else:
    print(f"\nВы проиграли! Загаданное число было: {secret_number}")
