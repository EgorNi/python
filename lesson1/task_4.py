number = int(input('введите целое положительное число'))
number3 = 0
while number > 0:
    number1 = number % 10
    number = number // 10
    if number1 > number3:
        number3 = number1
print(number3)








