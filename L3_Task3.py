
a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
def my_function(a, b, c):
    numbers = [a, b, c]
    numbers.remove(min(numbers))
    return(sum(numbers))
print(my_function(a, b, c))