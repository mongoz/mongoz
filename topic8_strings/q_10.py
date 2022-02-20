text = input('Введите текст: ')
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
constants = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

index = 0
frequent = 0

for ch in text:
    ch = ch.upper()
    # Индекс буквы в алфавите
    index = constants.find(ch)
    print(index)
# Накопитель количества
    if index >= 0:
        count[index] += 1


for i in range(len(count)):
    if count[i] > count[frequent]:
        print(count[i])
        frequent = i
print('Самый частый символ в строковом значении: ',
      constants[frequent], '.', sep='')

