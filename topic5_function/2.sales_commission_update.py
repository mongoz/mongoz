def get_price():
    price = float(input('Введите величину покупки: '))
    return price


def calc_tax(price):
    federal_tax = price * 0.05
    regional_tax = price * 0.025
    total_tax = federal_tax + regional_tax
    return federal_tax, regional_tax, total_tax


def deploy_result(price, federal_tax, regional_tax, total_tax):
    print(f"Cумма покупки ${price}")
    print(f"Cумма федерального налога ${federal_tax}")
    print(f"Cумма регионального налога ${regional_tax}")
    print(f"Cумма общего налога ${total_tax}")


def main():
    price = get_price()
    federal_tax, regional_tax, total_tax = calc_tax(price)
    deploy_result(price, federal_tax, regional_tax, total_tax)


main()