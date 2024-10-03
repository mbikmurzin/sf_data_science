import numpy as np

def binary_predict(number: int = 1) -> int:
    """Угадываем число с помощью бинарного поиска.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток.
    """
    count = 0
    low = 1
    high = 100

    while True:
        count += 1
        predict_number = (low + high) // 2  # середина диапазона
        if predict_number == number:
            break  # выход из цикла если угадали
        elif predict_number < number:
            low = predict_number + 1  # сдвигаем нижнюю границу
        else:
            high = predict_number - 1  # сдвигаем верхнюю границу
    return count


from typing import Callable  # добавим для аннотации типов

def score_game(predict_function: Callable[[int], int]) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм.

    Args:
        predict_function (Callable): функция угадывания.

    Returns:
        int: среднее количество попыток.
    """
    count_ls = []
    random_array = np.random.randint(1, 101, size=1000)  # загадали список чисел

    for number in random_array:
        count_ls.append(predict_function(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(binary_predict)
