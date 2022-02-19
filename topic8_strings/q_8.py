text = input('Введите строку: ').split()
l = ''
for i in text:
    l += i.capitalize() + ' '
print(l)
