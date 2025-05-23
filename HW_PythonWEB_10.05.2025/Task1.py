import random

list1 = [random.randint(1, 20) for _ in range(10)]
list2 = [random.randint(1, 20) for _ in range(10)]

print(f"List 1: {list1}")
print(f"List 2: {list2}")

combined = list1 + list2