def pyramid_calc(blocks):
    current_level = 1
    levels = 0
    while True:
        blocks -= current_level
        if blocks < 0:
            break
        levels += 1
        current_level += 1
    return levels


blocks = int(input("Enter the number of blocks: "))
levels = pyramid_calc(blocks)
print("The height of the pyramid:", levels)