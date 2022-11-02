"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def find_guessed_number(number: int = 1) -> int:
    """Находим загаданное число методом дихотомии (половинного деления)

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число шагов половинного деления
    """
    # количество попыток
    count = 0
    
    # левая граница поиска числа
    a = 1
    
    # правая граница поимка числа
    b = 101
    
    # отгадываемое число
    guessed_number = (a + b) // 2

    while True:
        count+=1       
        
        if guessed_number > number:
            b = guessed_number
            guessed_number = (guessed_number + a) // 2          
        elif guessed_number < number:
            a = guessed_number
            guessed_number = (b + guessed_number) // 2    
        else:                
            break #конец игры выход из цикла

    return count


def score_game(predict_function) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict_function ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел   

    for number in random_array:
        count_ls.append(predict_function(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(find_guessed_number)
   

