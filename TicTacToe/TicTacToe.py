#Tictactoe
import random

 #I needed something to store the player moves
movesPlayerX = []
movesPlayerO = []

print("Welcome to Tic-Tac-Toe!\nPlease select your first move to begin...")

#I needed something to get player input
def getPlayerInput():
    while True:
        try:
            return int(input("Please type your next move...\n"))
            break
        except:
            print("I'm sorry, that is not a number...\n")

#I needed something to check if either player had won
def hasPlayerWon(player):
    for x in (1, 4, 7):
        if x in player and x+1 in player and x+2 in player:
            return True
    for x in (1, 2, 3):
        if x in player and x+3 in player and x+6 in player:
            return True
    for x in (1, 3):
        if x in player and 5 in player and 10-x in player:
            return True
    return False

#I needed something that would get PLayer O's moves
def getAIMove():
    while True:
        newMove = random.randrange(1, 9, 1)
        if newMove not in movesPlayerO and newMove not in movesPlayerX:
            return newMove

#I wanted something to render the board
def Renderer():
    for w in (0, 1, 2):
        line = ""
        for y in range (3*w + 1 , 3*w + 4):
            if y in movesPlayerX:
                line = line + "X"
            elif y in movesPlayerO:
                line = line + "O"
            else:
                line = line + " "
        print(line)
    return None

#I needed something to put all the previous code together
for x in range (0,100):
    if x == 9:
        print("It's a draw!")
        break
    if x % 2 == 0:
        newPlayerMove = getPlayerInput()
        while True:
            if newPlayerMove not in movesPlayerX and newPlayerMove not in movesPlayerO:
                movesPlayerX.append(newPlayerMove)
                break
            else:
                print("Whoops! It appears that move has already been played!\n")
                newPlayerMove = getPlayerInput()
    else:
        newPlayerMove = getAIMove()
        print(newPlayerMove)
        movesPlayerO.append(newPlayerMove)
    Renderer()
    if hasPlayerWon(movesPlayerX):
        print("Player X has won!")
        break
    if hasPlayerWon(movesPlayerO):
        print("Player O has won!")
        break
    