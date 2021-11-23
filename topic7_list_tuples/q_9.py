def main():
    # Открыть файл
    file = open('USpopulation.txt', 'r', encoding='utf-8')

    # Cоздать пустой список
    pop_values = []

    # Перебрать значения из файла в список
    for i in file:
        pop_values.append(int(i.rstrip('\n')))

    annual_change = AnnualChange(pop_values)
    # Cреднегодовое изменение.
    total = 0
    for y in pop_values:
        total += y

    average = total / len(annual_change)
    print(f'Average annual change between 1950-1990 = {average:.2f}')
    print(f'The greatest increase is occurred in {annual_change.index(min(annual_change)) + 1951} '
          f'with an increase of {max(annual_change)}')
    print(f"The smallest increase in population occurred in {annual_change.index(min(annual_change)) + 1951} "
          f"with an increase of {min(annual_change)}")


def AnnualChange(pop_values):
    annual_change = [0] * (len(pop_values) - 1)
    # print(annual_change)

    index = 0

    while index < len(pop_values) - 1:
        annual_change[index] = pop_values[index + 1] - pop_values[index]
        index += 1
    return annual_change


main()
