import random
import os
letters = ["A","B","C"]
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]
options = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
plyr = 0
players = ["X","O"]
def menu():
    global plyr
    choice = input("TIC TAC TOE ...or\nNOUGHTS AND CROSSES\n===================\n1)Player vs Player\n2)Player vs Computer\nx)Quit\n\nPlease choose an option: ")
    newgame()
    if choice == "1":
        while True:
            mv = input("Player "+players[plyr%2]+" enter your move: ")
            if len(mv) != 2:
                print("Invalid move!\nPlease enter column followed by row. e.g. "+random.choice(letters)+str(random.randint(1,3)))
            elif not mv[1].isdigit():
                print("Invalid move!\nPlease enter column followed by row. e.g. "+random.choice(letters)+str(random.randint(1,3)))
            else:
                rc = get_row_col(mv)
                if check_and_place_move(rc, players[plyr%2]):
                    printboard()
                    check_win(players[plyr%2])
                    plyr += 1
                else:
                    print("Invalid move!\nPlease enter column followed by row. e.g. "+random.choice(letters)+str(random.randint(1,3)))
    elif choice == "2":
        while True:
            if players[plyr%2] == "X":
                mv = input("Player "+players[plyr%2]+" enter your move: ")
                if len(mv) != 2:
                    print("Invalid move!\nPlease enter column followed by row. e.g. "+random.choice(letters)+str(random.randint(1,3)))
                elif not mv[1].isdigit():
                    print("Invalid move!\nPlease enter column followed by row. e.g. "+random.choice(letters)+str(random.randint(1,3)))
                else:
                    rc = get_row_col(mv)
                    if check_and_place_move(rc, players[plyr%2]):
                        printboard()
                        check_win(players[plyr%2])
                        plyr += 1
                    else:
                        print("Invalid move!\nPlease enter column followed by row. e.g. "+random.choice(letters)+str(random.randint(1,3)))
            else:
                print(players[plyr%2]+"'s move:")
                cpumove(plyr)
                plyr += 1
    elif choice.upper() == "X":
        print("Good bye.")
        exit()
    else:
        print("Please choose a valid option")
def newgame():
    plyr = 0
    print("\nWhen entering move, please enter column followed by row. e.g. "+random.choice(letters)+str(random.randint(1,3))+"\n")
    for row in range(0,3):
        for col in range(0,3):
            board[row][col] = " "
    players = ["X","O"]
    global options
    options = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    printboard()
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
    print(boardstr)
def get_row_col(rowcol):
    if rowcol[0].upper() == "A":
        col = 0
    elif rowcol[0].upper() == "B":
        col = 1
    else:
        col = 2
    row = int(rowcol[1])-1
    return (row,col)
def check_and_place_move(rowcol, player):
    try:
        if 0 > rowcol[0] > 3 or 0 > rowcol[1] > 3:
            return False
        else:
            if board[rowcol[0]][rowcol[1]] == " ":
                board[rowcol[0]][rowcol[1]] = player
                options.remove(rowcol)
                return True
            else:
                return False
    except:
        return False
def check_win(player):
    win = False
    for row_or_col in range(0,3):
        #rows
        if board[row_or_col][0] == board[row_or_col][1] == board[row_or_col][2] == player:
            print("\n"+player + " is the winner!\n")
            win = True
            menu()
        #columns
        elif board[0][row_or_col] == board[1][row_or_col] == board[2][row_or_col] == player:
            print("\n"+player + " is the winner!\n")
            win = True
            menu()
    #diagonal
    if board[0][0] == board[1][1] == board[2][2] == player:
        print("\n"+player + " is the winner!\n")
        win = True
        menu()
    elif board[0][2] == board[1][1] == board[2][0] == player:
        print("\n"+player + " is the winner!\n")
        win = True
        menu()
    if not win and not " " in board[0] and not " " in board[1] and not " " in board[2]:
        print("\nDRAW!\nA strange game.\nThe only winning move is not to play.\n")
        menu()
def cpumove(player):
    rc = random.choice(options)
    if check_and_place_move(rc, players[player%2]):
        printboard()
        check_win(players[player%2])
    else:
        print("Error with CPU move!")
while True:
    menu()
