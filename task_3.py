# вариант 1
seasons = [
    ' ',
    'winter', 'winter',
    'spring', 'spring',
    'spring', 'summer',
    'summer', 'summer',
    'autumn', 'autumn',
    'autumn', 'winter']
user_time = int(input('Введите месяц в виде целого числа от 1 до 12: '))
print(seasons[user_time])

# вариант 2
seasons = {
    1: 'winter', 2: 'winter',
    3: 'spring', 4: 'spring',
    5: 'spring', 6: 'summer',
    7: 'summer', 8: 'summer',
    9: 'autumn', 10: 'autumn',
    11: 'autumn', 12: 'winter'}
user_time = int(input('Введите месяц в виде целого числа от 1 до 12: '))
print(seasons[user_time])
