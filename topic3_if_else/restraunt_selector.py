vegeterian = int(input('''Вы вегетарианец? Если "да", то нажмите 1, "нет" - 0'''))
vegan = int(input('''Вы вегaн? Если "да", то нажмите 1, "нет" - 0'''))
gluten = int(input('''Вы вегетарианец? Если "да", то нажмите 1, "нет" - 0'''))

result = vegeterian + vegan + gluten

if result == 0:
    print("Вот вариант")
    print("Изысканные гамбургеры от Джо")
elif result == 2:
    print("Вот вариант")
    print("Центральная пиццерия")
elif result == 3:
    print("Вот варианты")
    print("Кафе за углом")
    print("Кухня шеф-повара")