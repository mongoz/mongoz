budget = int(input('Сумма на месяц: '))
total = 0
saved = 0
again = 'y'
while again == 'y' or again == 'Y':
    purchase = int(input("Введите сумму покупки: "))
    total += purchase
    saved = budget - total
    again = input('Еще покупка?')

print('Cумма покупок =', total)
print('Остача денег =', saved)
