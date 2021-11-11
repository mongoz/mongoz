"""Программа чтения файлов со случайными числами. Выполнив предыдущее задание
(программу записи файла со случайными числами), напишите еще одну программу, которая
читает случайные числа из файла, выводит их на экран и затем показывает приведенные
ниже данные:
• сумму чисел;
• количество случайных чисел, прочитанных из файла."""


def main():
    total, quantity = count()
    display_file(total, quantity)


def count():
    total = 0
    quantity = 0
    file = open('number_1-500.txt', 'r')
    for i in file:
        total += int(i)
        quantity += 1
    return total, quantity


def display_file(total, quantity):
    file = open('number_1-500.txt', 'r')
    for i in file:
        print(i.rstrip('\n'))
    file.close()
    print(f"Сумма чисел {total}\n"
          f"Количество чисел {quantity}")


main()
