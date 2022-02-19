text = '''«Текст» — российский криминально-драматический
 психологический триллер режиссёра Клима Шипенко,
 экранизация романа-бестселлера
  «Текст» (2017) писателя Дмитрия Глуховского,
  который сам адаптировал свой роман в киносценарий.  
'''


def calc_text(textov):
    UPPER = 0
    LOWER = 0
    DIGITS = 0
    SPACE = 0

    for i in textov:
        if i.isupper():
            UPPER += 1
        elif i.islower():
            LOWER += 1
        elif i.isspace():
            SPACE += 1
        elif i.isdigit():
            DIGITS += 1
    print(F"Верхний регистр = {UPPER}\n"
          F"Нижний регистр = {LOWER}\n"
          F"Чисел = {DIGITS}\n"
          F"Пробелов = {SPACE}\n")


calc_text(text)
