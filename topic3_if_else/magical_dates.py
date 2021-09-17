day = int(input())
month = int(input())
year = int(input())

sum_date = day*month

if sum_date == year:
    print(f'{day}.{month}.{year} - Волшебная дата')
else:
    print(f'{day}.{month}.{year} - Обычная дата')