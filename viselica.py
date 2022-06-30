import random
popytki = 5
word_list = ['диван', 'холодильник', 'телевизор', 'кресло', 'стол', 'тумба', 'лампа', 'тостер', 'пылесос', 'кондиционер']
word = random.choice(word_list)

secret_word = list('*'*len(word))

while True:
    print(''.join(secret_word))
    print('Ваше количество попыток равно: ', popytki)
    bukva = input('Введите букву: ')
    if bukva in word:
        for i,c in enumerate(word):
            if c == bukva:
                secret_word[i] = bukva
        if '*' not in secret_word:
            print('Вы выиграли')
            break
    else:
        popytki -= 1
    if popytki == 0:
        print('Вы проиграли')
        break

