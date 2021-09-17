user_input = int(input('Ввеите к-ство секунд: '))

hours = 0
minutes = 0
seconds = 0
days = user_input // 86400
# Вычисляем остачу секунд в дне от введного количества секунд
day_remainder = user_input % 86400
if day_remainder > 0:
    hours = day_remainder // 3600
    hours_remainder = day_remainder % 3600

    if hours_remainder > 0:
        minutes = hours_remainder // 60
        minutes_remainder = hours_remainder % 60
        seconds = minutes_remainder

print(f'{user_input} секунд = Дней:{days} Часов:{hours} Минут:{minutes} Cекунд:{seconds}')
