print('программа для расчёта прогресса в днях')
day_start = int(input('введите текущий результат в км.'))
day_success = int(input('введите желаемый результат в км.'))
count = 1
while day_success > day_start:
    day_start *= 1.1
    count += 1
print(count)

