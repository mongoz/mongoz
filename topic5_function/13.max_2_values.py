def main():
    print('Cравним два числа!\n')
    user_number = int(input('Введите число: '))
    user_number_2 = int(input('Введите число: '))
    check_max(user_number, user_number_2)


def check_max(number_1, number_2):
    if number_1 < number_2:
        print(f'Число {number_2} больше.')
    else:
        print(f'Число {number_1} больше.')


main()