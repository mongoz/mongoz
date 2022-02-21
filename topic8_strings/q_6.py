def main():
    # Текст и конвертация в лист
    text = """Він народився у простій селянській хаті. її ледь було помітно серед золотих соняшників,
        ніжних мальв, бузини, порічок, аґрусу та іншої рослинності.
        Хата стояла на тихій вулиці села,
        яке є околицею містечка Сосниця на Чернігівщини."""
    text2 = text.split()
    print(text2)
    calculate(text)


def calculate(text2):
    # Переменные
    total_spot = 0
    # Количество точек
    for i in text2:
        if i.endswith('.'):
            total_spot += 1
    print(total_spot)

    # Cреднее количество слов
    average = len(text2) / total_spot
    print(f'{average}')


main()
