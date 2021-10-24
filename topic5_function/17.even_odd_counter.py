"""Счетчик четных/нечетных чисел. В этой главе вы увидели пример написания алгоритма,
который определяет четность или нечетность числа. Напишите программу, которая
генерирует 100 случайных чисел и подсчитывает количество четных и нечетных
случайных чисел"""

import random


def main():
    total_even_number = 0
    total_odd_number = 0
    for num in range(1, 101):
        number = generate_randomN()
        if (number % 2) == 0:
            total_even_number += 1
        else:
            total_odd_number += 1
    print(f'Общее к-во чётных чисел = {total_even_number}\n'
          f'Общее к-во нечётных чисел = {total_odd_number} ')


def generate_randomN():
    number = random.randint(1, 1000)
    return number


main()
