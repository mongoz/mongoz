def main():
    print('Автомобильные расходы за месяц:')
    car0 = float(input("1. Кредит: "))
    car1 = float(input("2. Страховка: "))
    car2 = float(input("3. Бензин: "))
    car3 = float(input("4. Машинное масло: "))
    car4 = float(input("5. Шины: "))
    car5 = float(input("6. Тех. обслуживание: "))
    sum_expenses(car0, car1, car2, car3, car4, car5)


def sum_expenses(car0, car1, car2, car3, car4, car5):
    sum_monthly = car0 + car1 + car2 + car3 + car4 + car5
    sum_year = sum_monthly * 12
    print(f'Сумма расходов за месяц на автомобиль = {sum_monthly}')
    print(f'Сумма расходов за год на автомобиль = {sum_year:.2f}')


main()
