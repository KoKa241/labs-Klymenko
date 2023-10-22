def tax_calc(income):
    if income < 0:
        tax = 0.0
    elif income <= 85528:
        tax = 0.18 * income - 556.02
    else:
        tax = 14839.02 + 0.32 * (income - 85528)
    return tax

income = float(input("Enter the annual income: "))
print("The tax is:", round(tax_calc(income), 0), "thalers")
