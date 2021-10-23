FEET = 12  # 1 фут = 12 дюймов.


def feet_to_inches(feet):
    inches = feet * 12
    return inches


def main():
    feet = float(input('Введите количество футов: '))
    inches = feet_to_inches(feet)
    print(f'{feet} футов = {inches:.1f} дюймов')


main()
