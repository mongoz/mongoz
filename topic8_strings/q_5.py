"""
Напишите программу, которая просит пользователя ввести 10-символьный номер телефона
в формате ХХХ-ХХХ-ХХХХ. Приложение должно показать номер телефона, в котором
все буквенные символы в оригинале переведены в их числовой эквивалент.
Например, если пользователь вводит 555-GET-FOOD, то приложение должно вывести
555-438-3663.
"""

phoneNum = input('Введи номер: ')
num_new1 = ''
num_new2 = ''
phoneNum = phoneNum.split('-')
print(phoneNum)
for i in phoneNum[1][0:]:
    for char in i:
        if char == 'A' or char == 'B' or char == 'C':
            char = '2'
        elif char == 'D' or char == 'E' or char == 'F':
            char = '3'
        elif char == 'G' or char == 'H' or char == 'I':
            char = '4'
        elif char == 'J' or char == 'K' or char == 'L':
            char = '5'
        elif char == 'M' or char == 'N' or char == 'O':
            char = '6'
        elif char == 'P' or char == 'Q' or char == 'R' or char == 'S':
            char = '7'
        elif char == 'T' or char == 'U' or char == 'V':
            char = '8'
        elif char == 'W' or char == 'X' or char == 'Y' or char == 'Z':
            char = '9'

        num_new1 += char.upper()

for i in phoneNum[2][0:]:
    for char in i:
        if char == 'A' or char == 'B' or char == 'C':
            char = '2'
        elif char == 'D' or char == 'E' or char == 'F':
            char = '3'
        elif char == 'G' or char == 'H' or char == 'I':
            char = '4'
        elif char == 'J' or char == 'K' or char == 'L':
            char = '5'
        elif char == 'M' or char == 'N' or char == 'O':
            char = '6'
        elif char == 'P' or char == 'Q' or char == 'R' or char == 'S':
            char = '7'
        elif char == 'T' or char == 'U' or char == 'V':
            char = '8'
        elif char == 'W' or char == 'X' or char == 'Y' or char == 'Z':
            char = '9'

        num_new2 += char.upper()

print(f'{phoneNum[0][0:]}-{num_new1}-{num_new2}')
