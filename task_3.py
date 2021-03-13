def my_func(num_1, num_2, num_3):
    my_sum = sum([num_1, num_2], num_3) - (min(num_1, num_2, num_3))
    return my_sum


user_number_1 = int(input('enter number_1: '))
user_number_2 = int(input('enter number_2: '))
user_number_3 = int(input('enter number_3: '))

print(my_func(user_number_1, user_number_2, user_number_3))
