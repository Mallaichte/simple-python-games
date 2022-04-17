import os
import random
import pathlib
import json

with open(str(pathlib.Path(__file__).parent.resolve())+"/answers.json","r") as read:
    answers = json.load(read)
print("Enter X to quit at any point.")
while True:
    category = input("Category: ").upper()
    if category == "X":
        exit()
    else:
        while True:
            answer = input("Category: "+category+"\nAnswer: ").upper()
            if answer == "X":
                break
            else:
                answers.append({"category":category,"answer":answer})
                with open(str(pathlib.Path(__file__).parent.resolve())+"/answers.json", "w") as save:
                    json.dump(answers, save)
