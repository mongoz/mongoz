"""
Чемпионы Мировой серии. Среди исходного кода главы 7, а также в подпапке data
"Решений задач по программированию" соответствующей главы вы найдете файл
WorldSeriesWinners.txt. Этот файл содержит хронологический список команд-победителей
Мировой серии по бейсболу с 1903 по 2009 годы. (Первая строка в файле является
названием команды, которая победила в 1903 году, а последняя строка является названием
команды, которая победила в 2009 году. Обратите внимание, что Мировая серия не
проводилась в 1904 и 1994 годах.)
Напишите программу, которая позволяет пользователю ввести название команды и
затем выводит количество лет, когда команда побеждала в Мировой серии в течение
указанного периода времени с 1903 по 2009 годы.
"""


def main():
    infile = open("WorldSeries.txt", "r", encoding='utf-8')

    # read the lines. eliminate \n by using splitlines()
    winners_list = infile.read().splitlines()

    search = input("Введите команду с большой буквы: ")

    # calculate the total winning
    total_winning = total_victories(winners_list, search)

    # print the results.
    print()
    print("Команда:", search, "была победителем", total_winning, "раз.")


def total_victories(winners_list, search):
    total_winning = 0
    index = 0

    while index < len(winners_list):
        if search == winners_list[index]:
            total_winning += 1
        index += 1
    return total_winning


main()
