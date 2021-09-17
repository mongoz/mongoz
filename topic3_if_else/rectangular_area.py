lenght1 = int(input())
lenght = int(input())
width1= int(input())
width = int(input())

area1 = lenght1*width1
area = lenght*width

if area > area1:
    print("Площадь 1-го больше")
elif area == area1:
    print("Прямоугольники равны")
else:
    print("Площадь 2-го больше")
