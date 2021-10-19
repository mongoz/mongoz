price = float(input('Введите величину покупки: '))
federal_tax = price * 0.05
regional_tax = price * 0.025
total_tax = federal_tax + regional_tax
print(f"Cумма покупки ${price}")
print(f"Cумма федерального налога ${federal_tax}")
print(f"Cумма регионального налога ${regional_tax}")
print(f"Cумма общего налога ${total_tax}")
