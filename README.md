def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль"
    return x / y

operations = {
    '1': ('Сложение', add),
    '2': ('Вычитание', subtract),
    '3': ('Умножение', multiply),
    '4': ('Деление', divide),
    '0': ('Выход', None)
}

def calculator():
    while True:
        print("\nВыберите операцию:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")

        choice = input("Введите номер операции: ").strip()

        if choice == '0':
            print("Выход из калькулятора.")
            break

        if choice not in operations:
            print("Ошибка: неверный выбор. Попробуйте снова.")
            continue

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: введите допустимые числа.")
            continue

        operation_name, operation_func = operations[choice]
        result = operation_func(num1, num2)
        print(f"Результат ({operation_name.lower()}): {result}")

if __name__ == "__main__":
    calculator()
