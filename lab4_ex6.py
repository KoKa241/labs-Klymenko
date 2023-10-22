from random import randint

def magic_num_game(num):
    while True:
        guess = int(input())
        if guess == num:
            print("Молодець, магле! Тепер ти вільний")
            break
        else:
            print("Ха-ха! Ви застрягли у моїй петлі!")


print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

magic_num = randint(1, 10)
magic_num_game(magic_num)
