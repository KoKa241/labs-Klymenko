from random import randint

def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  " , board[0][0] , "  |  " , board[0][1] , "  |  " , board[0][2] , "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  " , board[1][0] , "  |  " , board[1][1] , "  |  " , board[1][2] , "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  " , board[2][0] , "  |  " , board[2][1] , "  |  " , board[2][2] , "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")



def enter_move(board):
    move = int(input("Enter your move: "))
    x = (move - 1) // 3
    y = (move - 1) % 3
    move = (x, y)
    if move in make_list_of_free_fields(board):
        board[move[0]][move[1]] = "0"
    else:
        print("Invalid move!")
        enter_move(board)
    return board
    


def make_list_of_free_fields(board):
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " " or type(board[i][j]) == int:
                free_fields.append((i, j))
    return free_fields
   


def victory_for(board, sign):
    # Check rows
    for row in board:
        if all(cell == sign for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True

    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True

    return False


def draw_move(board):
    move = randint(1, 9)
    x = (move - 1) // 3
    y = (move - 1) % 3
    move = (x, y)
    if move in make_list_of_free_fields(board):
        print("Computer's move: ", move)
        board[move[0]][move[1]] = "X"
    else:
        draw_move(board)
    return board
    


def main():
    board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
    victory = False
    while victory == False:
        display_board(board)
        board = enter_move(board)
        board = draw_move(board)
        if victory_for(board, "0"):
            victory = True
            print("You won!")
        elif victory_for(board, "X"):
            victory = True
            print("Computer won!")

main()
