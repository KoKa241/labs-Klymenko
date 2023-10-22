def compute_func(x):
    y = 1 / (x + 1 / (x + 1 / (x + 1 / x + 1/2)))
    return y

x = [1, 10, 100, -5]
for num in x:
    y = compute_func(num)
    print("y = ", y)
