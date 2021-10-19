number = int(input("Введи позитивное число "))
factorial = 1
while number < 0:
    number = int(input(" Введи n>0 "))

for i in range(1, number + 1):
    factorial *= i

print(factorial)
