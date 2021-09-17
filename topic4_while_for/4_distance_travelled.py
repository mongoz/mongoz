speed = int(input('Скорость: '))
time = int(input('Время: '))
distance = 0
# while time != 0:
#     distance = speed*time
#     time -= 1
#     print(distance)
print(f'Час\tДистанция')
print('---------------')
for i in range(1, time+1):
    distance = speed * i
    print(f"{i}\t{distance}")