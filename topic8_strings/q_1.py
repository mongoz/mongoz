"""
Инициалы. Напишите программу, которая получает строковое значение, содержащее
имя, отчество и фамилию человека и показывает инициалы. Например, если пользователь
вводит Михаил Иванович Кузнецов, то программа должна вывести М.И.К.
"""

s = input().split()
print(s)
for i in s:
    print(i[0], end=".")
