"""Среднее арифметическое чисел. Допустим, что файл с рядом целых чисeл называется
numbers.txt и существует на диске компьютера. Напишите программу, которая вычисляет
среднее арифметическое всех хранящихся в файле чисел."""


def main():
    user_input = input("Введите имя файла: ")
    try:
        file = open(user_input, 'r', encoding='utf-8')
        count = 0
        total = 0
        for i in file:
            count += 1
            total += int(i)
        average = total / count
        print('Cреднее арифметическое =', average)
    except IOError as err:
        print(err)
    except ValueError as err:
        print(err)


main()
