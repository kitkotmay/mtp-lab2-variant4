import random
def play_game():
    """Запускает игру 'Угадай число'."""
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Я загадал число от 1 до 100.")
    print("Попробуйте его угадать.")
    while True:
        try:
            guess = int(input("Введите число: "))
        except ValueError:
            print("Нужно ввести целое число.")
            continue
        attempts += 1
        if guess < secret_number:
            print("Загаданное число больше.")
        elif guess > secret_number:
            print("Загаданное число меньше.")
        else:
            print("Вы угадали!")
            print(f"Количество попыток: {attempts}")
            break
if __name__ == "__main__":
    play_game()
