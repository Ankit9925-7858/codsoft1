import random

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-"*5)
    print()

def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True

    return False

def is_draw():
    return " " not in board

def player_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Invalid position!")
            elif board[move] != " ":
                print("Position already occupied!")
            else:
                board[move] = "X"
                break

        except ValueError:
            print("Enter a valid number!")

def ai_move():
    available = [i for i in range(9) if board[i] == " "]
    move = random.choice(available)
    board[move] = "O"
    print("AI chose position:", move + 1)

print("=== TIC TAC TOE AI ===")
print("You = X")
print("AI = O")

while True:

    print_board()

    player_move()

    if check_winner("X"):
        print_board()
        print("🎉 You Win!")
        break

    if is_draw():
        print_board()
        print("Game Draw!")
        break

    ai_move()

    if check_winner("O"):
        print_board()
        print("🤖 AI Wins!")
        break

    if is_draw():
        print_board()
        print("Game Draw!")
        break