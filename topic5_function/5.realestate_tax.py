A_VALUE = 0.60


def main():
    property_value = float(input("Фактическая цена недвижимости: "))
    a_amount = assessment_amount(property_value)
    calculate_tax(a_amount)


def assessment_amount(property_value):
    a_amount = property_value * A_VALUE
    print(f"Оценочная стоимость = ${a_amount}")
    return a_amount


def calculate_tax(a_amount):
    calc_tax = a_amount * 0.0072
    print(f'Налог на имущество = ${calc_tax:.2f}')
    return calc_tax


main()
