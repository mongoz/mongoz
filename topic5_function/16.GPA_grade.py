def main():
    n1 = int(input('Оценка 1-я: '))
    n2 = int(input('Оценка 2-я: '))
    n3 = int(input('Оценка 3-я: '))
    n4 = int(input('Оценка 4-я: '))
    n5 = int(input('Оценка 5-я: '))
    average_score = average(n1, n2, n3, n4, n5)
    determine_grade(n1, n2, n3, n4, n5)
    print(f'Средний бал = {average_score}')


def average(n1, n2, n3, n4, n5):
    average_score = (n1 + n2 + n3 + n4 + n5) / 5
    return average_score


def determine_grade(n1, n2, n3, n4, n5):
    for grade in (n1, n2, n3, n4, n5):
        if 90 <= grade <= 100:
            print(grade, "\t\t", "A")
        elif 90 <= grade <= 89:
            print(grade, "\t\t", "B")
        elif 70 <= grade <= 79:
            print(grade, "\t\t", "C")
        elif 60 <= grade <= 69:
            print(grade, "\t\t", "D")
        elif grade < 60:
            print(grade, "\t\t", "F")
        else:
            print('Вы ввели неверное значение.')


main()