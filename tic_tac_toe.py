from termcolor import colored

board = [1,2,3,'X',5,6,7,'O',9]
computer, player = "O", "X"
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
        
print_board()

def make_move(brd, plyr, mve, Undo = False):
    if can_move(brd, mve):
        brd[mve -1] = plyr
        win = is_winner(brd, plyr)
        if True:
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
        return True
            

def can_move(brd, mve):
    if mve in range(1, 10) and isinstance(brd[mve-1], int):
        return True
    return False

def has_empty_space():
    return board.count('X') + board.count('O') != 9