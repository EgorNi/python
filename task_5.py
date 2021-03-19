"""
Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("task_5.txt", "r+") as count_numbers:
    count_numbers.write('1 2 3 4 5')
with open("task_5.txt", "r+") as count_numbers:
    for i in count_numbers:
        x = list(map(int, i.split()))
    print(sum(x))
