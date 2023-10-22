my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

unique_list = []

for element in my_list:
    if element not in unique_list:
        unique_list.append(element)

my_list = unique_list.copy()

print("The list with unique elements only:")
print(my_list)
