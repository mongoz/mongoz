"""
Экзамен на получение водительских прав. Местный отдел по выдаче удостоверений на
право вождения автомобиля попросил вас создать приложение, которое оценивает письменную
часть экзамена на получение водительских прав. Экзамен состоит из 20 вопросов
с множественным выбором.
"""


def main():
    wright = ['A', 'C', 'A', 'A', 'D', 'B',
              'C', 'A', 'C', 'B', 'A', 'D',
              'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']  # Список правильных ответов
    user_solution = open('student_solution.txt', 'r')  # Открыть файл
    answer_wright, answer_wrong, wrong = count_answer(user_solution, wright)
    deploy_results(answer_wright, answer_wrong, wrong)


def count_answer(user_solution, wright):
    user_sol = []  # Cписок ответов пользователя
    answer_wright = 0  # Накопитель правильных ответов
    answer_wrong = 0  # Накопитель неправильных ответов
    wrong = []  # Cписок неправильных ответов
    # Перебор ответов студента в список
    for i in user_solution:
        user_sol.append(i.rstrip('\n'))

    for i in range(len(user_sol)):
        if user_sol[i] == wright[i]:
            answer_wright += 1
        else:
            answer_wrong += 1
            wrong.append(i + 1)
    return answer_wright, answer_wrong, wrong


def deploy_results(answer_wright, answer_wrong, wrong):
    if answer_wright < 15:
        print('Тест не пройден')
    else:
        print('Тест пройден')

    print(f"Правильных ответов {answer_wright}")
    print(f"Неправильных ответов {answer_wrong}")
    print(f'Номера неправильных ответов: ')
    for i in wrong:
        print(i, end=' ')


main()
