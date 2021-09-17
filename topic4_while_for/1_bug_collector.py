total = 0
days = 0
bug = 0
while days != 5:
    bug = int(input(f'Количество багов за {days+1} день = '))
    total += bug
    days += 1
print(f'Количество ошибок за 5 дней = {total}')
