from termcolor import colored

board = list(range(1, 10))
winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
           (0, 3, 6), (1, 4, 7), (2, 5, 8),
           (0, 4, 8), (2, 4, 6))
moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))

player, computer = "X", "O"

def print_board():
    for i in range(0, 9, 3):
        for j in range(3):
            val = board[i + j]
            if val == "X":
                print(colored(f"[{val}]", "red"), end=" ")
            elif val == "O":
                print(colored(f"[{val}]", "blue"), end=" ")
            else:
                print(f"[{val}]", end=" ")
        print("\n---------")

def make_move(brd, plyr, mve, undo=False):
    if can_move(brd, mve):
        brd[mve - 1] = plyr
        win = is_winner(brd, plyr)
        if undo:
            brd[mve - 1] = mve
        return True, win
    return False, False

def can_move(brd, mve):
    return mve in range(1, 10) and isinstance(brd[mve - 1], int)

def is_winner(brd, plyr):
    for tup in winners:
        if all(brd[i] == plyr for i in tup):
            return True
    return False

def has_empty_space():
    return board.count("X") + board.count("O") != 9

def computer_move():
    mv = -1
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            mv = i
            break
    if mv == -1:
        for j in range(1, 10):
            if make_move(board, player, j, True)[1]:
                mv = j
                break
    if mv == -1:
        for tup in moves:
            for m in tup:
                if mv == -1 and can_move(board, m):
                    mv = m
                    break
    return make_move(board, computer, mv)

# ---- Game Start ----
print("Player: X\nComputer: O\n")

while has_empty_space():
    print_board()
    try:
        move = int(input("Choose your move (1-9): "))
    except ValueError:
        print("Invalid input!\n")
        continue

    moved, won = make_move(board, player, move)
    if not moved:
        print("Invalid move! Try again.\n")
        continue
    if won:
        print_board()
        print(colored("You won!", "green"))
        break
    moved, won = computer_move()
    if won:
        print_board()
        print(colored("You lose!", "yellow"))
        break

else:
    print_board()
    print(colored("It's a draw!", "cyan"))
