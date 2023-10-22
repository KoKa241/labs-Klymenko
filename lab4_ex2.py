def greater(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "The numbers are equal"
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(greater(num1, num2))
