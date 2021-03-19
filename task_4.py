"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
dictionary = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
result_on_russian = []
with open('task_4.txt', 'r+', encoding='utf-8') as rewrite:
    for i in rewrite.readlines():
        x = i.split(' - ')
        print(x)
        if x[0] in dictionary:
            rus_world = dictionary[x[0]]
            result_on_russian.append(rus_world + ' - ' + x[1])
    print(result_on_russian)
    new_file = open("task_4_1.txt", "w")
    new_file.writelines(result_on_russian)
    new_file.close()
