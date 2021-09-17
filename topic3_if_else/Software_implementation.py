user_input = int(input('К-ство приобретенных программ: '))
software_package = 99
total_price = software_package*user_input
if user_input == 0:
    print('Скидки нет')
elif 10 <= user_input <= 19:
    print('Cкидка 10%')
    sale_price = total_price - (total_price*0.1)
    print(f'Цена {sale_price}')
elif 20 <= user_input <= 49:
    print('Cкидка 20%')
    sale_price = total_price - (total_price*0.2)
    print(f'Цена {sale_price}')
elif 50 <= user_input <= 99:
    print('Cкидка 30%')
    sale_price = total_price - (total_price*0.3)
    print(f'Цена {sale_price}')
elif user_input >= 100:
    print('Cкидка 40%')
    sale_price = total_price - (total_price*0.4)
    print(f'Цена {sale_price}')
else:
    print('К-ство покупок недостаточно для скидки')
