def recursive_sum(n):
    """Рекурсивно вычисляет сумму чисел от 1 до n."""
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)
def main():
    number = int(input("Введите положительное целое число: "))
    if number < 0:
        print("Число должно быть неотрицательным.")
        return
    result = recursive_sum(number)
    print(f"Сумма чисел от 1 до {number}: {result}")
if __name__ == "__main__":
    main()
