"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json
total_inf = [{}, {}]

with open('task_7.txt') as company_inf:
    for i in company_inf.readlines():
        name, shape_own, profit, spent_money = i.split()
        total_inf[0][name] = int(profit) - int(spent_money)
    total_inf[1]['average_profit'] = sum(
        x for y, x in total_inf[0].items() if x > 0) / len(total_inf[0])

    print(total_inf)
with open('task_7.json', 'w') as company_inf_js:
    json.dump(total_inf, company_inf_js)
