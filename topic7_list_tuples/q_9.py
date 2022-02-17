"""
Данные о населении. Среди исходного кода главы 7, а также в подпапке data "Решений
задач по программированию" соответствующей главы вы найдете файл USPopulation.txt.
Этот файл содержит данные о среднегодовой численности населения США в тысячах с
1950 по 1990 годы. Первая строка в файле содержит численность населения в 1950 году,
вторая строка - численность населения в 1951 году и т. д.
Напишите программу, которая считывает содержимое файла в список. Программа должна
показать приведенные ниже данные:
• среднегодовое изменение численности населения в течение указанного периода времени;
• год с наибольшим увеличением численности населения в течение указанного периода
времени;
• год с наименьшим увеличением численности населения в течение указанного периода
времени.
"""


def main():
    # Открыть файл
    file = open('USpopulation.txt', 'r', encoding='utf-8')
    pop_values = create(file)
    average = calculate_v(pop_values)
    values(pop_values, average)


def create(file):
    # Cоздать пустой список
    pop_values = []

    # Перебрать значения из файла в список
    for i in file:
        pop_values.append(int(i.rstrip('\n')))

    return pop_values


def calculate_v(pop_values):
    # Cреднегодовое изменение.
    # Cумма
    total = 0
    for i in pop_values:
        total += i

    average = total / len(pop_values)
    return average


def values(pop_values, average):
    maximum_value = max(pop_values)
    minimum_value = min(pop_values)

    max_value_indx = pop_values.index(maximum_value)
    min_value_indx = pop_values.index(minimum_value)
    print(min_value_indx)
    print(max_value_indx)

    print(f'Average annual change between 1950-1990 = {average:.2f}')
    print(f'The greatest increase is occurred in {max_value_indx + 1951}'
          f' with an increase of {max(pop_values)}')
    print(f'The smallest increase in population occurred in {min_value_indx + 1951}'
          f' with an increase of {min(pop_values)}')


def AnnualChange():
    pass
    # annual_change = [0] * (len(pop_values) - 1)
    # print(annual_change)

#   index = 0

#   while index < len(pop_values) - 1:
#    annual_change[index] = pop_values[index + 1] - pop_values[index]
#    index += 1
#   print(annual_change)
#   return annual_change
