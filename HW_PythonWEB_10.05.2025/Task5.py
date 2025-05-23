user_input = input("\nEnter list elements separated by spaces: ")
elements = user_input.split()

numbers_list = []
for el in elements:
    try:
        numbers_list.append(int(el))
    except ValueError:
        print(f"Warning! '{el}' is not an integer and will be skipped.")
print("List of numbers:", numbers_list)
print("--------------------------")

target = int(input("Enter a number to search for: "))

count_target = 0
for num in numbers_list:
    if num == target:
        count_target += 1
print(f"The number {target} appears {count_target} time(s) in the list.")
print("--------------------------")

# Task 6
total_sum = 0
for num in numbers_list:
    total_sum += num
print(f"Total_sum: {total_sum}")
print("--------------------------")

average = total_sum / len(numbers_list) if numbers_list else 0
print(f"average: {average}")
print("--------------------------")
