my_list = []

while True:
    try:
        user_input = int(input("Введіть елемент (-1 для завершення введення): "))

        if user_input == -1:
            break  
        else:
            my_list.append(user_input)

    except ValueError:
        print("Введіть коректне ціле число.")

def bubble_sort(input_list):
    n = len(input_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
    
    return input_list


print(bubble_sort(my_list))
