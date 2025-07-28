from termcolor import colored

board = [1,2,3,'X',5,6,7,'O',9]
computer, player = "O", "X"

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
        
print_board()

def make_move(brd, plyr, mve, Undo = False):
    if can_move(brd, mve):
        brd[mve -1] = plyr
        win = is_winner(brd, plyr)


def has_empty_space():
    return board.count('X') + board.count('O') != 9