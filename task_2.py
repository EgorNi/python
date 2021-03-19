"""
Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
"""

my_count = open('task_2.txt.')
count_words = 0
for i in my_count.readlines():
    count_words += len(i.split())
    print(len(i.split()))
my_count.close()
