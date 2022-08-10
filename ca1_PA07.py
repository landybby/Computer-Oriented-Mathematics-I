import random

positions = [['Z',0],['ZH',4],['H',10],['HH',14]]

def updatePosition(n,m,pos,rnd):
    if rnd >= 0 and rnd < 0.25:
        if (pos + 1) % m == 0:
            pos = pos - (m - 1)
        else:
            pos += 1
    elif rnd >= 0.25 and rnd < 0.5:
        if pos % m == 0:
            pos += (m - 1)
        else:
            pos -= 1
    elif rnd >= 0.5 and rnd < 0.75:
        if (pos + m) >= (m * n):
            pos = pos - (n - 1) * m
        else:
            pos += m
    elif rnd >= 0.75 and rnd < 1:
        if (pos - m) < 0:
            pos = pos + (n - 1) * m
        else:
            pos -= m
    return pos 

def updatePositions(n,m,positions):
    for i in range(0,len(positions)):
        positions[i][1] = updatePosition(n,m,positions[i][1],random.random())
def sortPositions(positions):
    i = 1
    while i > 0:
        i = 0
        for s in range(0, len(positions) - 1):
            a = positions[s]
            b = positions[s + 1]
            if a[1] > b[1]:
                positions[s] = b
                positions[s + 1] = a
                i += 1
           
def extractSquare(positions):
    square = []
    square.append(positions[-1])
    positions.pop(-1)
    for i in range(0, len(positions)):
        if positions[-1][1] == square[0][1]:
            square.append(positions[-1])
            positions.pop(-1)
    return(square)

def giftExchange(square):
    zh = 0
    h = 0
    for i in range(0,len(square)):
        if square[i][0] == "ZH":
            zh += 1
        elif square[i][0] == "H" or square[i][0] == "HH":
            h += 1
    if zh > 0 and h > 0:
        for i in range(0,len(square)):
            if square[i][0] == "H":
                square[i][0] = "HH"
    z = 0
    hh = 0
    for i in range(0,len(square)):
        if square[i][0] == "Z":
            z += 1
        elif square[i][0] == "HH":
            hh += 1
    if z >= 2 * hh:
        for i in range(0,len(square)):
            if square[i][0] == "H":
                square[i][0] = "Z"
            elif square[i][0] == "HH":
                square[i][0] = "Z"
    else: 
        for i in range(0,len(square)):
            if square[i][0] == "Z":
                    square[i][0] = "ZH"

def christmasFated(positions):
    z = 0
    zh = 0
    for i in range(0,len(positions)):
        if positions[i][0] == "Z":
            z += 1
        elif positions[i][0] == "ZH":
            zh += 1
    if (z + zh) == len(positions):
        return True
    elif z == 0:
        return True
    else: 
        return False

def mergeSquare(square,intermediate):
    for i in range(0, len(square)):
        intermediate.append(square[0])
        square.pop(0)
        
def christmasFate(positions):
    z = 0
    for i in range(0,len(positions)):
        if positions[i][0] == "Z":
            z += 1
    if z == 0:
        return("Ho, ho, ho, and a merry Zombie-Christmas!")
    else:
        return("Zombies ate my Christmas!")
        
def zombieChristmas(n,m,positions):
    while christmasFated(positions) == False:
        updatePositions(n,m,positions)
        sortPositions(positions)
        intermediate = []
        while len(positions) != 0:
            square = extractSquare(positions)
            giftExchange(square)
            mergeSquare(square,intermediate)
        positions = intermediate
    return christmasFate(positions)