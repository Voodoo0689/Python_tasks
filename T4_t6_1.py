from itertools import cycle

my_list = [True, 'ABC', 123, None]
i = 0
for el in cycle(my_list):
    i += 1
    if i < 1000:
        print(el)

