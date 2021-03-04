money = int(input('введите сумму выручки'))
not_money = int(input('введите сумму издержек'))
if money > not_money:
    print('вы работаете с прибылью')
    print('подсчитаем рентабельность')
    rent = int(input('введите количество персонала'))
    print('ваша рентабельность ', round(money / rent))
else:
    print('вы работаете с убытками')
