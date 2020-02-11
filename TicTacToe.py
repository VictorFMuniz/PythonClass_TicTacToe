# This program is a TicTacToe game intended to be a practice for the Python course


#Preparing variables to represent the table
#
# a1 | a2 | a3
# ------------
# b1 | b2 | b3
# ------------
# c1 | c2 | c3

a1 = " "
a2 = " "
a3 = " "
b1 = " "
b2 = " "
b3 = " "
c1 = " "
c2 = " "
c3 = " "

def printTable():
    print(
          " " + a1 + " | " + a2 + " | " + a3 +"\n" +
          "------------\n"+
          " " + b1 + " | " + b2 + " | " + b3 +"\n" +
          "------------\n"+
          " " + c1 + " | " + c2 + " | " + c3
          )

def getPos(player):
    pos = ""
    while True:

        pos = input("Player " + str(player) +", choose your position according to the map: ")
        if pos not in ("a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"):
            print("A posiçâo inserida não é válida:" + pos)
        else:
            break
    return pos

def winCon():
    if((a1 == "x" and b1 == "x" and c1 == "x") or (a1 == "o" and b1 == "o" and c1 == "o")):
        return a1
    if ((a2 == "x" and b2 == "x" and c2 == "x") or (a2 == "o" and b2 == "o" and c2 == "o")):
        return a2
    if ((a3 == "x" and b3 == "x" and c3 == "x") or (a3 == "o" and b3 == "o" and c3 == "o")):
        return a3
    if ((a1 == "x" and a2 == "x" and a3 == "x") or (a1 == "o" and a2 == "o" and a3 == "o")):
        return a1
    if ((b1 == "x" and b2 == "x" and b3 == "x") or (b1 == "o" and b2 == "o" and b3 == "o")):
        return b1
    if ((c1 == "x" and c2 == "x" and c3 == "x") or (c1 == "o" and c2 == "o" and c3 == "o")):
        return c1
    if ((a1 == "x" and b2 == "x" and c3 == "x") or (a1 == "o" and b2 == "o" and c3 == "o")):
        return a1
    if ((a3 == "x" and b2 == "x" and c1 == "x") or (a3 == "o" and b2 == "o" and c1 == "o")):
        return a3

def runGame():

    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3

    print("Table Map:\n" 
          "a1 | a2 | a3\n"
          "------------\n"
          "b1 | b2 | b3\n"
          "------------\n"
          "c1 | c2 | c3\n"
          )

    printTable()

    pos = getPos(1)b2

    if pos == "a1":
        a1 = "x"
    if pos == "a2":
        a2 = "x"
    if pos == "a3":
        a3 = "x"
    if pos == "b1":
        b1 = "x"
    if pos == "b2":
        b2 = "x"
    if pos == "b3":
        b3 = "x"
    if pos == "c1":
        c1 = "x"
    if pos == "c2":
        c2 = "x"
    if pos == "c3":
        c3 = "x"

    printTable()

    win = winCon()
    if win in ("x","o"):
        return win

    pos = getPos(2)

    if pos == "a1":
        a1 = "o"
    if pos == "a2":
        a2 = "o"
    if pos == "a3":
        a3 = "o"
    if pos == "b1":
        b1 = "o"
    if pos == "b2":
        b2 = "o"
    if pos == "b3":
        b3 = "o"
    if pos == "c1":
        c1 = "o"
    if pos == "c2":
        c2 = "o"
    if pos == "c3":
        c3 = "o"

    printTable()

    win = winCon()
    if win in ("x", "o"):
        return win




print("Welcome to TicTacToe 3000\n")
while True:
    win = runGame()
    if win in ("x" ,"o"):
        break

print(win+" is the winner!")