def calc_insurance(value):
    insurance = value * 0.8
    print(f"Минимальная страховую сумма = ${insurance:.2f}")


def main():
    price = float(input('Стоимость недвижимого имущества: '))
    calc_insurance(price)


main()
