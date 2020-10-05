a = float(input("Ведите првую переменную"))
b = float(input("Введите вторую переменную"))
what = input("Выберите дествие + или -")

if what == "-":
    c = a - b
    print(c)
elif what == "+":
    c = a + b
    print(c)
else:
    print("Не верная операция")



