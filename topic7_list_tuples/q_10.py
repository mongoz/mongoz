def main():
    infile = open("WorldSeries.txt", "r", encoding='utf-8')

    # read the lines. eliminate \n by using splitlines()
    winners_list = infile.read().splitlines()

    search = input("Введите команду с большой буквы: ")

    # calculate the total winning
    total_winning = CalculateTotalWinning(winners_list, search)

    # print the results.
    print()
    print("Команда:", search, "была победителем", total_winning, "раз.")


def CalculateTotalWinning(winners_list, search):
    total_winning = 0

    index = 0
    while index < len(winners_list):
        if search == winners_list[index]:
            total_winning += 1
        index += 1
    return total_winning


main()
