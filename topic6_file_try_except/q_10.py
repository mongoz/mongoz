"""Очки в игре в гольф. Любительский гольф-клуб проводит турниры каждые выходные.
Президент клуба попросил вас написать две программы:
• программу, которая читает имя каждого игрока и его счет в игре, вводимые с клавиатуры,
и затем сохраняет их в виде записей в файле golf.txt (каждая запись будет иметь
поле для имени игрока и поле для счета игрока);
• программу, которая читает записи из файла golf.txt и выводит их на экран."""
import q_10_1 as d


def golf_file():
    try:
        file_output = open('golf.txt', 'w', encoding='utf-8')

        player_name = input('Введите имя игрока или 0 для выхода: ')
        while player_name != "0":
            file_output.write(f"{player_name}\t")

            player_score = int(input(f'Введите результат для игрока {player_name}: '))
            player_name = input('Введите имя игрока или 0 для выхода: ')

            file_output.write(f"{str(player_score)}\n")
        file_output.close()
        return file_output
    except Exception as err:
        print(err)


def main():
    golf_file()
    print(f'Вся информация о игроках записана в файл golf.txt')
    d.display_player()


main()
