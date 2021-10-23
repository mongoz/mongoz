""" Оценщик малярных работ. Малярная компания установила, что на каждые 10 квадратных
метров поверхности стены требуется 5 литров краски и 8 часов работы. Компания
взимает за работу 2000 руб. в час. Напишите программу, которая просит пользователя
ввести площадь поверхности окрашиваемой стены и цену 5-литровой емкости краски.
Программа должна показать следующие данные:
• количество требующихся емкостей краски;
• количество требующихся рабочих часов;
• стоимость краски;
• стоимость работы;
• общая стоимость малярных работ."""

PAN_L = 5
ONE_HOUR = 2000
TEN_METRS_TIME = 8
AREA = 10


def main():
    wall_area = float(input('Введите площадь поверхности: '))
    paint_price = float(input('Стоимость 5 литровой банки с краской: '))
    pan = round(calc_paint(wall_area))
    work_hours = calc_time(wall_area)
    print(f'Количество банок для {wall_area} кв.м. = {pan}\n'
          f'Количество рабочих часов для {wall_area} кв.м = {work_hours}')
    calc_others(paint_price, work_hours, pan)


def calc_paint(wall_area):
    one_metr_litr = PAN_L / AREA  # Количество краски на 1 метр.
    litr_area = one_metr_litr * wall_area  # Литров краски на всю поверхность
    pans = litr_area / PAN_L  # Количество банок
    return pans


def calc_time(wall_area):
    hours_to_minutes = TEN_METRS_TIME * 60  # минуты затраченные на 10 кв.м.
    one_metr_time = hours_to_minutes // 10  # затраченное время на 1 кв.м.
    work_time_minutes = wall_area * int(one_metr_time)
    work_hours_minutes = work_time_minutes // 60
    return work_hours_minutes


def calc_others(paint_price, work_hours, pan):
    work_price = ONE_HOUR * work_hours  # стоимость работы
    pan_price = paint_price * pan
    total_price = work_price + pan_price
    print(f'Cтоимость {pan} банок краски = ${pan_price:.2f}\n'
          f'Cтоимость работы = ${work_price:.2f}\n'
          f'Общая стоимость малярных работ = ${total_price:.2f}')


main()
