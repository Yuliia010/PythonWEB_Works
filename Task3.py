import random

numbers = [random.randint(-10, 10) for _ in range(15)]
print("List:", numbers)
print("--------------------------")

even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print("Even numbers:", even_numbers)
print("--------------------------")

odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
print("Odd numbers:", odd_numbers)
print("--------------------------")

negative_numbers = []
for num in numbers:
    if num < 0:
        negative_numbers.append(num)
print("Negative numbers:", negative_numbers)
print("--------------------------")

positive_numbers = []
for num in numbers:
    if num > 0:
        positive_numbers.append(num)
print("Positive numbers:", positive_numbers)
print("--------------------------")
