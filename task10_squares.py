def create_squares(n):
    """Создаёт словарь вида число: квадрат числа."""
    return {number: number ** 2 for number in range(1, n + 1)}
def main():
    n = int(input("Введите N: "))
    if n < 1:
        print("N должно быть положительным числом.")
        return
    squares = create_squares(n)
    print("Словарь квадратов:")
    for number, square in squares.items():
        print(f"{number}: {square}")
if __name__ == "__main__":
    main()
