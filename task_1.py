def division(num_1, num_2):
    if num_2 == 0:
        try:
            num_1 / 0
        except ZeroDivisionError:
            return print('division by zero!')
    else:
        return print(num_1 / num_2)


number_1 = int(input('enter one number: '))
number_2 = int(input('enter one number: '))
division(number_1, number_2)
