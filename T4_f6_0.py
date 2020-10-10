from itertools import count

for el in count(int(input('Введите стартовое число '))):
    if el < 1000:
        print(el)
