"""Обработка исключений. Измените программу, которую вы написали для задания 6
таким образом, чтобы она обрабатывала приведенные ниже исключения:
• она должна обрабатывать любые исключения IOError, которые вызываются, когда
файл открыт, и данные из него считываются;
• она должна обрабатывать любые исключения ValueError, которые вызываются, когда
прочитанные из файла значения конвертируются в числовой тип."""


def main():
    user_input = input("Введите имя файла: ")
    try:
        file = open(user_input, 'r', encoding='utf-8')
        count = 0
        total = 0
        for i in file:
            count += 1
            total += int(i)
        average = total / count
        print('Cреднее арифметическое =', average)
    except IOError as err:
        print(err)
    except ValueError as err:
        print(err)


main()
