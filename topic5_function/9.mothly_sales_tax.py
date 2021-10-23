FED_TAX = 0.05
MUN_TAX = 0.025


def main():
    total_month_sale = float(input('Общая cумма продаж за месяц: '))
    calc_tax(total_month_sale)


def calc_tax(total_month_sale):
    federal_tax = FED_TAX * total_month_sale
    municipal_tax = MUN_TAX * total_month_sale
    total_tax = federal_tax + municipal_tax
    print(f'Общая сумма продаж за месяц = ${total_month_sale}\n'
          f'Сумма федерального налога   = ${federal_tax:.2f}\n'
          f'Сумма муниципального налога = ${municipal_tax:.2f}\n'
          f'Общий налог за месяц продаж = ${total_tax:.2f}')


main()