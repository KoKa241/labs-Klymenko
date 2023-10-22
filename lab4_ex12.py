def hypothesis_collatz(num):
    steps = 0
    while True:
        if num == 1:
            return True
        elif num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        steps += 1
        print(num, "steps:", steps)

hypothesis_collatz(100)
