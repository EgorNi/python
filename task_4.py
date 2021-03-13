# option 1
def exponentiation(x, y):
    exp = 1 / (x ** y)
    return exp


numb_1 = int(input('enter number'))
numb_2 = int(input('enter a negative integer'))
print(exponentiation(numb_1, numb_2))


# option_2
def exponentiation_2(x, y):
    my_exp = 1
    while y != 0:
        my_exp *= x
        y += 1
    return my_exp


user_numb_1 = int(input('enter number'))
user_numb_2 = int(input('enter a negative integer'))
print(exponentiation_2(user_numb_1, user_numb_2))
