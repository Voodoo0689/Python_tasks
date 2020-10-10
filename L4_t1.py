#Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
#Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv



output = int(argv[1])
fix_award = int(argv[2])
bonus = int(argv[3])



def money(output, fix_award, bonus):
    res = (output * fix_award) + bonus
    return res

print(money(output, fix_award, bonus))




