import random

numbers = [random.randint(-10, 10) for _ in range(15)]
print("List:", numbers)

sum_negative = 0
for num in numbers:
    if num < 0:
        sum_negative += num

print("Sum negative:", sum_negative)
print("--------------------------")

sum_even = 0
for num in numbers:
    if num % 2 == 0:
        sum_even += num
print("Sum even:", sum_even)
print("--------------------------")

sum_odd = 0
for num in numbers:
    if num % 2 != 0:
        sum_odd += num
print("Sum odd:", sum_odd)
print("--------------------------")

product_index_3 = 1
for i in range(0, len(numbers)):
    if i % 3 == 0:
        product_index_3 *= numbers[i]
print("Product index 3:", product_index_3)
print("--------------------------")

min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
start = min(min_index, max_index) + 1
end = max(min_index, max_index)
product_between_min_max = 1
if start < end:
    for i in range(start, end):
        product_between_min_max *= numbers[i]
else:
    product_between_min_max = 0 

print("Product between min max:", product_between_min_max)
print("--------------------------")

first_positive = -1
last_positive = -1
for i in range(len(numbers)):
    if numbers[i] > 0:
        if first_positive == -1:
            first_positive = i
        last_positive = i

sum_between_positives = 0
if first_positive != -1 and first_positive < last_positive:
    for i in range(first_positive + 1, last_positive):
        sum_between_positives += numbers[i]
print("Sum between positives:", sum_between_positives)
print("--------------------------")


