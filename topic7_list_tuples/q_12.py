user = 10

num_list = []
simple_list = [2]
# Заполним список числами до введенного числа
for i in range(2, user+1):
    num_list.append(i)


for i in range(2, user + 1):
    k = 0
    # Проверим числа в списке на простоту.
    for j in simple_list:
        if i % j == 0:
            k = 1
    if k == 0:
        simple_list.append(i)
        print(i, 'Простое число')


print(num_list)
print(simple_list)