from random import randint

def main():
    john_apples = randint(0, 100)
    mary_apples = randint(0, 100)
    adam_apples = randint(0, 100)
    print(john_apples, mary_apples, adam_apples)
    total_apples = john_apples + mary_apples + adam_apples
    print(f"Total apples: {total_apples}")

main()
