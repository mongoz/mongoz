days = int(input('Количество отработанных дней: '))
total = 0
coin = 0.01
print("День Зарплата")
for current_day in range(1, days + 1, 1):
    print(f'{current_day}\t{coin} руб.')
    coin *= 2
    total += coin
print('----------------------------------------')
print(f"Зарплата за 30 дней = {total:,.2f} рубля")



