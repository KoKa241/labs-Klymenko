def main():
    input_num_one = int(input("Enter a number 1: "))
    input_num_two = int(input("Enter a number 2: "))
    if input_num_one < input_num_two:
        print(input_num_two)
    elif input_num_one > input_num_two:
        print(input_num_one)
    else:
        print('Nums is equal')

if __name__ == '__main__':
    main()
