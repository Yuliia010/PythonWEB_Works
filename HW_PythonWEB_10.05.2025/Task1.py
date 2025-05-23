import random

list1 = [random.randint(1, 20) for _ in range(10)]
list2 = [random.randint(1, 20) for _ in range(10)]

print(f"List 1: {list1}")
print(f"List 2: {list2}")
print("-------------------------------------")
combined = list1 + list2

print(f"Combined: {combined}")

print("-------------------------------------")
combined_no_duplicates = list()
for item in combined:
    if item not in combined_no_duplicates:
        combined_no_duplicates.append(item)

print(f"Combined no duplicates: {combined_no_duplicates}")

print("-------------------------------------")
common_elements = []
for item in list1:
    if item in list2 and item not in common_elements:
        common_elements.append(item)

print(f"Common elements: {common_elements}")
print("-------------------------------------")
unique_elements = []
for item in list1:
    if list1.count(item) == 1:
        unique_elements.append(item)

for item in list2:
    if list2.count(item) == 1:
        unique_elements.append(item)

unique_elements_no_duplicates = []
for item in unique_elements:
    if item not in unique_elements_no_duplicates:
        unique_elements_no_duplicates.append(item)

print(f"Unique elements: {unique_elements_no_duplicates}")
print("-------------------------------------")
min1 = list1[0]
max1 = list1[0]
for item in list1:
    if item < min1:
        min1 = item
    if item > max1:
        max1 = item

min2 = list2[0]
max2 = list2[0]
for item in list2:
    if item < min2:
        min2 = item
    if item > max2:
        max2 = item

min_max_values = [min1, max1, min2, max2]

print(f"Min and Max values: {min_max_values}")
print("-------------------------------------")


