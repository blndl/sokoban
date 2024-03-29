from copy import *

class coords:  #2d coordinates class
    def __init__(self, x, y):
        self.x = x
        self.y = y

def printMap (level):
    for xs in level:
        print(" ".join(map(str, xs)))

def findPlayer(level):  #returns player position
    xy = coords(0,0)
    for buf in level:
        xy.y = 0
        for f in buf:
            if f == 2 or f == 6:
                break
            xy.y += 1
        if f == 2 or f == 6:
            break
        xy.x += 1
    return (xy)

# movement and crate pushing

def moveLeft(level):
    xy = findPlayer(level)
    if level[xy.x][xy.y - 1] == 0 or level[xy.x][xy.y - 1] == 4:
        level[xy.x][xy.y] -= 2
        level[xy.x][xy.y - 1] += 2
        print("Moved left.\n")
    elif level[xy.x][xy.y - 1] == 3 or level[xy.x][xy.y - 1] == 7:
        handlePush(level, 1)
    else:
        print("Failed to move\n")
    
def moveRight(level):
    xy = findPlayer(level)
    if level[xy.x][xy.y + 1] == 0 or level[xy.x][xy.y + 1] == 4:
        level[xy.x][xy.y] -= 2
        level[xy.x][xy.y + 1] += 2
        print("Moved right.\n")
    elif level[xy.x][xy.y + 1] == 3 or level[xy.x][xy.y + 1] == 7:
        handlePush(level, 2)
    else:
        print("Failed to move\n")

def moveUp(level):
    xy = findPlayer(level)
    if level[xy.x - 1][xy.y] == 0 or level[xy.x - 1][xy.y] == 4:
        level[xy.x][xy.y] -= 2
        level[xy.x - 1][xy.y] += 2
        print("Moved up.\n")
    elif level[xy.x - 1][xy.y] == 3 or level[xy.x - 1][xy.y] == 7:
        handlePush(level, 3)
    else:
        print("Failed to move\n")

def moveDown(level):
    xy = findPlayer(level)
    if level[xy.x + 1][xy.y] == 0 or level[xy.x + 1][xy.y] == 4:
        level[xy.x][xy.y] -= 2
        level[xy.x + 1][xy.y] += 2
        print("Moved down.\n")
    elif level[xy.x + 1][xy.y] == 3 or level[xy.x + 1][xy.y] == 7:
        handlePush(level, 4)
    else:
        print("Failed to move\n")
    

def handlePush(level, path):
    if path == 1:
        pushLeft(level)
    elif path == 2:
        pushRight(level)
    elif path == 3:
        pushUp(level)
    elif path == 4:
        pushDown(level)

def pushLeft(level):
    xy = findPlayer(level)
    if level[xy.x][xy.y - 2] == 0 or level[xy.x][xy.y - 2] == 4:
        level[xy.x][xy.y - 1] -= 3
        level[xy.x][xy.y - 2] += 3
        moveLeft(level)

def pushRight(level):
    xy = findPlayer(level)
    if level[xy.x][xy.y + 2] == 0 or level[xy.x][xy.y + 2] == 4:
        level[xy.x][xy.y + 1] -= 3
        level[xy.x][xy.y + 2] += 3
        moveRight(level)


def pushUp(level):
    xy = findPlayer(level)
    if level[xy.x - 2][xy.y] == 0 or level[xy.x - 2][xy.y] == 4:
        level[xy.x - 1][xy.y] -= 3
        level[xy.x - 2][xy.y] += 3
        moveUp(level)

def pushDown(level):
    xy = findPlayer(level)
    if level[xy.x + 2][xy.y] == 0 or level[xy.x + 2][xy.y] == 4:
        level[xy.x + 1][xy.y] -= 3
        level[xy.x + 2][xy.y] += 3
        moveDown(level)

def winCheck(level): #win condition
    blockCheck = 0
    goalCheck = 0
    fullCheck = 0
    for line in level:
        if 3 in line:
            blockCheck += 1
        if 4 in line or 6 in line:
            goalCheck += 1
        if 7 in line:
            fullCheck += 1
    if blockCheck == 0 and goalCheck == 0 and fullCheck > 0:
        return 1
    else:
        return 0

def gameLoop(level):
    game = 1
    moves = 0
    while game == 1:
        printMap(level)
        answer = input("1.Left  2.Right\n3.Up  4.Down")
        if answer == "1":
            moveLeft(level)
        elif answer == "2":
            moveRight(level)
        elif answer == "3":
            moveUp(level)
        elif answer == "4":
            moveDown(level)
        moves += 1
        if winCheck(level) == 1:
            game = 0
            printMap(level)
            print("victory in ", moves,"moves\n")
            return (1)

def adventureLoop(levels): #multi level loop
    lvl = 0        
    for i in levels:
        lvl += 1
        adventure = 1
        menu = 1
        while menu == 1:
            print("level ", lvl,"\n")
            answer = input("1.Start  2.Quit 3.Help")
            if answer == "1":
                print("Good luck for level ", lvl, "!")
                gameLoop(i)
                menu = 0
            elif answer == "2":
                print("quitting adventure mode")
                menu = 0
                adventure = 0
                break
            elif answer == "3":
                help()
            else:
                print("Invalid answer")
        if adventure == 0:
            break


def help():
    print("As the Player(2) walk through the empty spaces(0) and push the crates(3) on the goals(4).\n\nDont get then stuck next to walls(1) !") 

def mainMenu(levels):
    inMenu = 1
    while inMenu == 1:
        answer = input("Welcome to Sokoban !\n1.Play 3 maps  2.Help  3.Quit\n")
        playLevel = deepcopy(levels)
        if answer == "1":
            adventureLoop(playLevel)
        elif answer == "2":
            help()
        elif answer == "3":
            inMenu = 0
