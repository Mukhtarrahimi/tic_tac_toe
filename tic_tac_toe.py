from termcolor import colored

board = [1,2,3,4,5,6,7,8,9]
winner = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (3,5,8), (0,4,8), (2,4,6))

def print_board():
    j = 1
    for i in board:
        end = " "
        if j % 3 == 0:
            end = "\n\n"
        if i == "X":
            print(colored(f"[{i}],", 'red'), end=end)
        elif i == "O":
            print(colored(f"[{i}],", 'blue'), end=end)
        else:
            print(f"[{i}]", end=end)
        j += 1
        
def make_move(brd, plyr, mve, Undo = False):
    if can_move(brd, mve):
        brd[mve -1] = plyr
        win = is_winner(brd, plyr)
        if Undo:
            brd[mve -1] = mve
        return True , win
    return False, False
        
def is_winner(brd, plyr):
    win = True
    for tup in winner:
        win = True
        for j in tup:
            if brd[j] != plyr:
                win = False
                break
            if win:
                break
        return win
        
        
def can_move(brd, mve):
    if mve in range(1, 10) and isinstance(brd[mve-1], int):
        return True
    return False

def has_empty_space():
    return board.count('X') + board.count('O') != 9


computer, player = "O", "X"
print("Player: X\nComputer: O")

while has_empty_space():
    print_board()
    move = int(input("Choose your move(1-9): "))
    moved, won = make_move(board, player, move)
    if not moved:
        print("invalid input! Try again!")
        continue
    if won:
        print(colored("you won!", "green"))
        break