chess_board = [[1 if (row == 0 or row == 7) and (col == 0 or col == 7) else "_" for col in range(8)] for row in range(8)]

for row in chess_board:
    print(" ".join(map(str, row)))
