def main():
    days = 7
    values = get_values(days)
    # calculate_values(values)


def get_values(days):
    total = 0
    my_list = []
    day = 1
    while day <= days:
        values = int(input(f'Введите сумму продаж за {day}-й рабоч. день недели: '))
        my_list.append(values)
        day += 1
        total += values
    print(f'Значения сохранены в переменную "my_list"')
    print(my_list)
    print(f'Общий объем продаж = {total}')
    return my_list

    # def calculate_values(values):
    # total = 0
    # for v in values:
    #     total += v
    # print(f'Общий объем продаж = {total}')


main()
