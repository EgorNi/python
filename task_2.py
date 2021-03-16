previous_list = [1, 333, 15, 3, 2021, 90, 16, 1000, 999, 1001]
new_list = [x for x in previous_list if x > previous_list[previous_list.index(x) - 1]]
print(new_list)
