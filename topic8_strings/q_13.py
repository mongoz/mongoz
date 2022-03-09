"""
•1 Средняя цена за год: вычисляет среднюю цену бензина за год для каждого года
в файле. (Данные файла начинаются апрелем 1993 и заканчиваются августом 2013.
Используйте данные, предоставленные за период с 1993 по 2013 годы.)
• Средняя цена за месяц: вычисляет среднюю цену в каждом месяце в файле.
• Наибольшая и наименьшая цены в году: в течение каждого года в файле определяет
дату и величину самой низкой и самой высокой цены.
"""
STARTING_YEAR = 1993
ENDING_YEAR = 2013


def get_price_data(gas):
    # Получил только цены
    gas_prices = []  # Цены
    gas_data = []  # Дата
    for i in range(len(gas)):
        value = gas[i].strip('\n').split(':')
        print(value)
        gas_prices.append(float(value[1]))
        gas_data.append(value[0])

    return gas_prices, gas_data


def get_years(data):
    print('Года')
    # Добавим только года
    gas_years = []
    for j in range(len(data)):
        gas_years.append(int(data[j].split('-')[2]))
    print(gas_years)

    return gas_years


def get_months(data):
    print('Месяцы')
    gas_months = []
    for j in range(len(data)):
        gas_months.append(int(data[j].split('-')[0]))
    print(gas_months)

    return gas_months


def get_yearly_average(prices, years, months):
    # Cпособ.1 через юзера по индексу
    total_prices = 0
    total_month = 0
    user_input = int(input("Показать среднюю цену за год: "))
    while user_input != int(user_input):
        print('Вы допустили ошибку')
        user_input = int(input('Введи год правильно: '))
    # Общая цена за год
    t = 0
    while years.index(user_input) == prices.index(years.index(user_input)]:
        for i in prices:
            total_prices += i
            t += 1
    print(f"Количество месяцев = {total_month}")
    print(f"Общая цена = {total_prices}")
    # print(f"Средняя цена за {user_input} год = {average_year}")


def main():
    file_gas = open('GasPrices.txt', 'r')
    gas = file_gas.readlines()
    # Цена
    prices, data = get_price_data(gas)
    # Года
    years = get_years(data)
    # Месяцы
    months = get_months(data)
    # Cреднее за год
    get_yearly_average(prices, years, months)


main()
