import numpy as np


def score_game(game_core_func):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core_func(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


def game_core(number):
    """Сначала устанавливаем середину множества, а потом уменьшаем или увеличиваем его пополам в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 0
    mid = 50
    predict = mid
    while True:
        count += 1
        if number > predict:
            predict += mid
        elif number < predict:
            predict -= mid
        mid = np.math.ceil(mid / 2)  # делим шаг пополам и округляем в большую сторону

        if number == predict:
            return count  # выход из цикла, если угадали


# запускаем
score_game(game_core)

