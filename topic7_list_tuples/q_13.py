import random


def main():
    file = open('answers.txt', 'r', encoding='utf-8')
    a = gen_list_answers(file)
    ball_answer(a)


# Генерация списка
def gen_list_answers(file):
    answers = []
    # Добавить в список
    for i in file:
        answers.append(i.rstrip('\n'))
    return answers


# Рандомный ответ
def ball_answer(answers):
    user = input('Введите ДА или Нет или нажмите ENTER для выхода: ')
    while user == 'да' or user == 'нет':
        num = random.randint(0, len(answers))
        print(answers[num])
        user = input('Введите ДА или Нет или нажмите ENTER для выхода: ')
