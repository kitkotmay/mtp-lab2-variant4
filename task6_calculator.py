def calculate(first, second, operation):
    """Выполняет выбранную арифметическую операцию."""
    if operation == "+":
        return first + second
    if operation == "-":
        return first - second
    if operation == "*":
        return first * second
    if operation == "/":
        if second == 0:
            raise ValueError("Деление на ноль невозможно.")
        return first / second
    raise ValueError("Неизвестная операция.")
def main():
    first = float(input("Введите первое число: "))
    operation = input("Введите операцию (+, -, *, /): ")
    second = float(input("Введите второе число: "))
    try:
        result = calculate(first, second, operation)
        print(f"Результат: {result}")
    except ValueError as error:
        print(f"Ошибка: {error}")
if __name__ == "__main__":
    main()
