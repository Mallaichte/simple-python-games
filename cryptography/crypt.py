import os
import random
import pathlib
import json
with open(str(pathlib.Path(__file__).parent.resolve())+"/answers.json","r") as read:
    answers = json.load(read)
author = ""
answer = ""
masked = ""
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
remainingletters = alpha
playerkey = {"A":"-","B":"-","C":"-","D":"-","E":"-","F":"-","G":"-","H":"-","I":"-","J":"-","K":"-","L":"-","M":"-","N":"-","O":"-","P":"-","Q":"-","R":"-","S":"-","T":"-","U":"-","V":"-","W":"-","X":"-","Y":"-","Z":"-"}
key = {}
unmaskkey = {}

def mask():
    # Create key
    global key
    global author
    global answer
    global masked
    alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    maskalpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for keyletter in alpha:
        maskletter = random.choice(maskalpha)
        key.update({keyletter:maskletter})
        unmaskkey.update({maskletter:keyletter})
        maskalpha.remove(maskletter)
    #print(key)
    # Select quote
    choice = random.choice(answers)
    author = choice["author"]
    answer = choice["text"]
    # Mask quote
    masked = ""
    #print(author + " - " + answer)
    for i in range(len(answer)):
        if answer[i].upper() in alpha:
            masked += key[answer[i].upper()]
        else:
            masked += answer[i]
    print(author + " - " + masked)

def unmask(ukey):
    alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    unmaskstr = ""
    for i in range(len(masked)):
        if masked[i] in alpha:
            unmaskstr += ukey[masked[i]]
        else:
            unmaskstr += masked[i]
    if unmaskstr.upper() == answer.upper():
        print("\n"+author+" - "+answer+"\nYou have decrypted the quote!")
        newgame()
    return unmaskstr

def updateremainingletters():
    global remainingletters
    remainingletters = alpha
    checkstring = unmask(playerkey)
    for c in alpha:
        if c in checkstring or not unmaskkey[c] in masked:
            remainingletters.remove(c)

def playermove():
    global playerkey
    global remainingletters
    maskletter = input("Which letter do you want to replace? : ").upper()
    if maskletter == "!C":
        updateremainingletters()
        #maskletter = random.choice(remainingletters)
        maskletter = input("Which letter would you like to reveal? : ").upper()
        replaceletter = unmaskkey[maskletter]
        print(maskletter+" will be replaced by "+replaceletter)
    elif maskletter == "!A":
        unmask(unmaskkey)
    else:
        replaceletter = input("Which letter do you want to replace "+maskletter+" with? : ").upper()
    playerkey.update({maskletter:replaceletter})
    print("ENCRYPTED: "+masked+" - "+author+"\nDECRYPTED: "+unmask(playerkey))

def newgame():
    global playerkey 
    playerkey = {"A":"-","B":"-","C":"-","D":"-","E":"-","F":"-","G":"-","H":"-","I":"-","J":"-","K":"-","L":"-","M":"-","N":"-","O":"-","P":"-","Q":"-","R":"-","S":"-","T":"-","U":"-","V":"-","W":"-","X":"-","Y":"-","Z":"-"}
    ans = input("Would you like to try a difficult cryptography challenge? [y/n]: ").upper()
    if ans == "N":
        print("Good bye!")
        quit()
    else:
        mask()
        while True:
            playermove()

newgame()
