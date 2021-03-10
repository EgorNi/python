user_text = input('Введите несколько слов: ')
user_words = user_text.split()
for n, word in enumerate(user_words, 1):
    print(n, word[:10])
