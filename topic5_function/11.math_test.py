import random


def main():
    first_number = random.randint(1, 1000)
    second_number = random.randint(1, 1000)
    print('Привет!\nРеши тест.\nСколько будет:\n'
          f'  {first_number}\n+ {second_number}')
    total = calc_numbers(first_number, second_number)
    user_number = int(input('Введи ответ: '))
    result_check(total, user_number)


def calc_numbers(first_number, second_number):
    total = first_number + second_number
    return total


def result_check(total, user_number):
    if user_number == total:
        print('Поздравляю!\nВы угадали.')
    else:
        print('К сожалению, ты допустил ошибку =).')


main()
