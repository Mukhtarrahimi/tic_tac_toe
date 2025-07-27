board = [1,2,3,4,5,6,7,8,9]
computer, player = "O", "X"

def print_board():
    j = 1
    for i in board:
        end = " "
        if j % 3 == 0:
            end = "\n\n"
        print(f"[{i}]", end=end)
        j += 1
            
print_board()