user_list = list(input('Введите элементы списка: '))
for rps_el in range(1, len(user_list), 2):
    user_list[rps_el - 1], user_list[rps_el] = user_list[rps_el], user_list[rps_el - 1]
print(user_list)
