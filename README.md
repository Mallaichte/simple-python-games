# Simple python games
Play tic tac toe or hangman in the console

## Tic Tac Toe
### 2022-04-16
I was working through the challenges on [Python Principles](https://pythonprinciples.com/challenges/) when I came across [one](https://pythonprinciples.com/challenges/Tic-tac-toe-input/) that challenges you to convert a player string into a tuple ("A3"=(2,0)) for the imagined purpose of creating a tic-tac-toe game. So I put my attempt in and then challenged myself to expand that into an actual tic-tac-toe game that you can play in the console.

Almost extactly 1hr 45 mins later, I had a version I was happy with.

Next logical step will be to allow the player to play versus the computer.

### 2022-04-17
I got woke up early by dog this morning. I couldn't get back to sleep after I took her out. My stupid brain kept telling me that it'd written the player vs cpu code and I better get up and add it to the script otherwise it'd keep nagging me. So I did. CPU chooses randomly from available spaces.

I'll add difficulty levels later. Easy: it prioritises placing its mark wherever it might be possible to complete the game first. Medium: it prioritises moves by defence and trying to create maximum opportunity (e.g. going for 3 corners). Hard: it uses my daughter's devious tactics of misdirection and creating traps. Impossible: Basically going against WOPR from [WarGames](https://www.imdb.com/title/tt0086567/). The CPU plays defensively, blocking all possible from the player. (The computer won't explicitly try and win on Impossible, it will just make sure that you can't.)

I'm going to go back to bed now!

## Hang man
### 2022-04-17 (afternoon)
I didn't get back to sleep, but I didn't work on tic-tac-toe either. I made hangman instead. Fill a json file with samples and the computer will randomly select a Hangman for you to solve.

### 2022-04-17 (Evening)
I've updated the answers.json with a larger selection of answers and created a tool (add_answers.py) to add additional answers to the file more easily.


