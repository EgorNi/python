time = int(input('введите время в секундах'))
hours = round(time % 3600)
minutes = time % 60
seconds = time % 10
print('переформатируем в привычный формат времени')
print(f'{hours}:{minutes}:{seconds}')

