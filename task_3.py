"""
Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

my_count = open('task_3.txt', encoding='utf-8')
count_average = []
count_poor_colleagues = []
for i in my_count:
    count = i.split()
    if float(count[int(1)]) < 20000:
        count_poor_colleagues.append(count[0])
    count_average.append(float(count[int(1)]))
count_average = sum(count_average) / len(count_average)
print('poor colleagues are: ', count_poor_colleagues)
print('average salary is:', round(count_average))
my_count.close()
