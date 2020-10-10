numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [el for i, el in enumerate(numbers) if i > 0 and numbers[i - 1] < numbers[i]]
print(result)

result_2 = [num1 for num1, num2 in zip(numbers[1:], numbers[:-1]) if num1 > num2]
print(result_2)