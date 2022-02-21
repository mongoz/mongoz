my_string = 'ПРОСПАЛ ПОЧТИ ВСЮ НОЧЬ'.split()
print(my_string)
my_list = []
total = ''

for i in range(len(my_string)):
    k = my_string[i][1:] + my_string[i][0] + 'КИ'
    total += k + ' '
print(total)
