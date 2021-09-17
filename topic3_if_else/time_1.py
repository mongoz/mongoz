user_input = int(input('Ввеите к-ство секунд'))

if user_input >= 60:
    minutes = user_input // 60
    print(f'{minutes} в {user_input} cекундах')
elif user_input >= 3600:
    hours = user_input // 3600
    print(f'{hours} в {user_input} cекундах')
elif user_input >= 86400:
    days = user_input // 86400
    print(f'{days} в {user_input} cекундах')