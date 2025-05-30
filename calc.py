ex = input("Введите выражение (например, 2 + 3): ")

try:
    num_1, op, num_2 = ex.split()
    num_1 = float(num_1)
    num_2 = float(num_2)

    if op == '+':
        res = num_1 + num_2
    elif op == '-':
        res = num_1 - num_2
    elif op == '*':
        res = num_1 * num_2
    elif op == '/':
        if num_2 == 0:
            print("Ошибка: на ноль деление невозможно")
        else:
            res = num_1 / num_2
    else:
        print("Ошибка: Неподдерживаемая операция!")
    
    if 'res' in locals():
        print(f"Результат: {res}")

except ValueError:
    print("Ошибка формата ввода. Пожалуйста, введите выражение в формате: число оператор число")