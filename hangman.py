import os
import random
import pathlib
import json
with open(str(pathlib.Path(__file__).parent.resolve())+"/answers.json","r") as read:
	answers = json.load(read)
category = ""
answer = ""
masked = ""
letters = ""
lives = 6
head = " " #o
body = " " #|
leftarm = " " #-
rightarm = " " #-
leftleg = " " #/
rightleg = " " #\\
done = False

def gal():
    gallows = "\n  |----¬   "+category+"\n  |    "+head+"\n  |   "+leftarm+body+rightarm+"  "+letters+"\n  |   "+leftleg+" "+rightleg+"  "+str(lives)+" attempts left\n__|__\n"
    print(gallows)

def mask():
    global category
    global answer
    global masked
    choice = random.choice(answers)
    category = choice["category"]
    answer = choice["answer"]
    for char in range(len(answer)):
        if answer[char] == " ":
            masked += "/"
        elif answer[char] in ",:'&.!?;()":
            masked += answer[char]
        else:
            masked += "-"

def newgame():
    print("Please note that a double forwardslash (//) indicates a hyphen(-)")
    global catgory, answer, masked, letters, lives, head, body, leftarm, rightarm, leftleg, rightleg, done
    done = False
    category = ""
    answer = ""
    masked = ""
    letters = ""
    lives = 6
    head = " " #o
    body = " " #|
    leftarm = " " #-
    rightarm = " " #-
    leftleg = " " #/
    rightleg = " " #\\
    mask()
    gal()
    print(masked)
    player_guess()

def gameover():
    print("\n\nGAME OVER\n"+answer+"\n  ( x x )\n     ^")
    global done
    done = True
    menu()

def win():
    print("\n\nYou win!\n"+answer+"\n  ( o o )\n     W")
    global done
    done = True
    menu()
def wrong_answer():
    global lives, head, body, leftarm, rightarm, leftleg, rightleg
    lives -= 1
    if head == " ":
        head = "o"
    elif body == " ":
        body = "|"
    elif leftarm == " ":
        leftarm = "-"
    elif rightarm == " ":
        rightarm = "-"
    elif leftleg == " ":
        leftleg = "/"
    else:
        rightleg = "\\"
    if lives  == 0:
        gameover()

def check_character(char):
    global masked
    global answer
    if char.upper() in answer.upper():
        for c in range(len(answer)):
            if answer[c].upper() == char.upper():
                masked= masked[:c]+char.upper()+masked[c+1:]
        if not "-" in masked:
            win()
    else:
        wrong_answer()
def player_guess():
    global letters
    while not done:
        guess = input("Please enter your guess: ")
        letters += guess
        check_character(guess)
        gal()
        print(masked)
def menu():
    if input("Play a game of hang man? [Y/N]: ").upper()[0] == "Y":
        newgame()
    else:
        print("\nGood bye!\n")
        exit()

menu()
