var_1 = float(input("Enter a number: "))
var_2 = float(input("Enter a number: "))

print("The sum of the numbers is: ", var_1 + var_2)
print("The difference of the numbers is: ", var_1 - var_2)
print("The product of the numbers is: ", var_1 * var_2)
try:
    print("The quotient of the numbers is: ", var_1 / var_2)
except ZeroDivisionError:
    print("Can't divide by zero")

print("\nThat's all, folks!")
