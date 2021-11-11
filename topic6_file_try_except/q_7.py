"""Программа записи файла со случайными числами. Напишите программу, которая
пишет в файл ряд случайных чисел . Каждое случайное число должно быть в диапазоне
от 1 до 500. Приложение должно предоставлять пользователю возможность назначать
количество случайных чисел, которые будут содержаться в файле."""
import random


def main():
    user_in = int(input('Введите количество чисел: '))
    write_file(user_in)
    display_file()


def write_file(user_in):
    file = open('number_1-500.txt', 'w')
    for i in range(user_in):
        number = random.randint(1, 500)
        file.write(f'{str(number)}\n')
    print('Числа записаны в файл.')
    file.close()


def display_file():
    file = open('number_1-500.txt', 'r')
    for i in file:
        print(i.rstrip('\n'))
    file.close()


main()
