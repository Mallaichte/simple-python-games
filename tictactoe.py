import random
letters = ["A","B","C"]
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]
players = ["X","O"]
def newgame():
    print("When entering move, please enter column followed by row. e.g. "+random.choice(letters)+str(random.randint(1,3)))
    for row in range(0,3):
        for col in range(0,3):
            board[row][col] = " "
    printboard()
    players = ["X","O"]
def printboard():
    boardstr = "    A   B   C   \n  -------------\n"
    c = 1
    for row in board:
        boardstr += str(c)+" | "
        for col in row:
            boardstr += col + " | "
        boardstr += str(c)+"\n  -------------\n"
        c +=1
    boardstr += "    A   B   C   "
    print(boardstr.rstrip(""))
def get_row_col(rowcol):
    if rowcol[0].upper() == "A":
        col = 0
    elif rowcol[0].upper() == "B":
        col = 1
    else:
        col = 2
    row = int(rowcol[1])-1
    return (row,col)
def check_and_place_move(row, col, player):
    if 0 > row > 3 or 0 > col > 3:
        return False
    else:
        if board[row][col] == " ":
            board[row][col] = player
            return True
        else:
            return False
def check_win(player):
    win = False
    for row_or_col in range(0,3):
        #rows
        if board[row_or_col][0] == board[row_or_col][1] == board[row_or_col][2] == player:
            print("\n"+player + " is the winner!\n")
            win = True
            newgame()
        #columns
        elif board[0][row_or_col] == board[1][row_or_col] == board[2][row_or_col] == player:
            print("\n"+player + " is the winner!\n")
            win = True
            newgame()
    #diagonal
    if board[0][0] == board[1][1] == board[2][2] == player:
        print("\n"+player + " is the winner!\n")
        win = True
        newgame()
    elif board[0][2] == board[1][1] == board[2][0] == player:
        print("\n"+player + " is the winner!\n")
        win = True
        newgame()
    if not win and not " " in board[0] and not " " in board[1] and not " " in board[2]:
        print("\nDRAW!\n")
        newgame()
newgame()
plyr = 0
while True:
    mv = input("Player "+players[plyr%2]+" enter your move: ")
    if len(mv) != 2:
        print("Invalid move!\nPlease enter column followed by row. e.g. "+random.choice(letters)+str(random.randint(1,3)))
    elif not mv[1].isdigit():
        print("Invalid move!\nPlease enter column followed by row. e.g. "+random.choice(letters)+str(random.randint(1,3)))
    else:
        rc = get_row_col(mv)
        if check_and_place_move(rc[0],rc[1], players[plyr%2]):
            printboard()
            check_win(players[plyr%2])
            plyr += 1
        else:
            print("Invalid move!\nPlease enter column followed by row. e.g. "+random.choice(letters)+str(random.randint(1,3)))
