def gcd(a, b):
    """Возвращает наибольший общий делитель двух чисел."""
    while b != 0:
        a, b = b, a % b
    return abs(a)
def main():
    first = int(input("Введите первое число: "))
    second = int(input("Введите второе число: "))
    result = gcd(first, second)
    print(f"НОД чисел {first} и {second}: {result}")
if __name__ == "__main__":
    main()
