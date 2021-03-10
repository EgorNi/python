my_list = [1, 2, 3, 9, 6]
user_number = int(input('Введите новый элемент рейтинга: '))
my_list.append(user_number)
my_list = sorted(my_list)
my_list.reverse()
print(my_list)
