import random


def main():
    print(f"Игра \"Угадай число от 1 до 100!\"")
    print('Число сгенерировано.')
    user_number = int(input('Ваш ответ: '))
    number = generateRandom()
    check_answer(user_number, number)

    again = 'Д'
    total = 1
    while again == 'Д':
        user_number = int(input('Ваш ответ: '))
        if not check_answer(user_number, number):
            total += 1
            prompt = input('Подсказка нужна? (Д): \n')
            if get_prompt(prompt):
                print(number)
                break
            again = input('Ещё попытка? (Д): \n')
        else:
            print('Поздравляю! Вы угадали!')

    print(f'Количество догадок = {total}')


def generateRandom():
    number = random.randint(1, 101)
    return number


def check_answer(user_number, number):
    if user_number < number:
        print('Слишком мало, пробуйте ещё раз.\n')
        status = False
    elif user_number > number:
        print('Cлишком много, пробуйте ещё раз.\n')
        status = False
    else:
        status = True
    return status


def get_prompt(prompt):
    if prompt == 'Д':
        status = True
    else:
        status = False
    return status


main()
