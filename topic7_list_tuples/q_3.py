"""
Статистика дождевых осадков. Разработайте программу, которая позволяет пользователю
занести в список общее количество дождевых осадков за каждый из 12 месяцев.
Программа должна вычислить и показать суммарное количество дождевых осадков за
год, среднее ежемесячное количество дождевых осадков и месяцы с самым высоким и
самым низким количеством дождевых осадков.
"""


def main():
    months = ['Январь', 'Февраль', 'Март',
              'Апрель', 'Май', 'Июнь', 'Июль',
              'Август', 'Сентябрь', 'Октябрь',
              'Ноябрь', 'Декабрь']
    # print(months)
    list_mod(months)


def list_mod(months):
    list_values = []
    total = 0
    m = 0  # месяц
    while m <= len(months) - 1:
        user_input = float(input(f'Введите к-о осадков за {months[m]}: '))
        list_values.append(user_input)
        total += user_input
        m += 1
    # print(list_values)
    average = total / len(months)
    min_month = months[list_values.index(min(list_values))]
    max_month = months[list_values.index(max(list_values))]

    min_value = min(list_values)
    max_value = max(list_values)
    print(f"Total rainfall this year = {total:.2f}\n"
          f"Average rainfall this year = {average:.2f}\n"
          f"The month with the highest rainfall this year - {max_month} = {max_value:.2f}\n"
          f"The month with the lowest rainfall this year - {min_month} = {min_value:.2f}")


main()
