products = []
shop = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analitics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
cnt = 0
while True:
    if input('Выход - Q, \nY - продолжить: ').upper() == 'Q':
        break
    cnt += 1
    for f in shop.keys():
        user_data = input(f'{f}: ')
        shop[f] = int(user_data) if (f == 'цена' or f == 'количество') else user_data
        analitics[f].append(shop[f])
    products.append((cnt, shop.copy()))
    print('Текущая аналитика по товарам:\n')
    for key, value in analitics.items():
        print(key, value)
print(products)
