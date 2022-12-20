import re, math, copy
f = open("input.txt", "r")
print("hello day 9")

Hpos = [0,0]
Tpos = []
for i in range(9):
    Tpos.append([0,0])
stops = {}

def moveSegment(tail, move, next):
    #print(Tpos)
    yMath = move[0] - Tpos[tail][0]
    xMath = move[1] - Tpos[tail][1]
    if abs(yMath) + abs(xMath) > 2:
        Tpos[tail][1] = Tpos[tail][1] + (xMath/abs(xMath))
        Tpos[tail][0] = Tpos[tail][0] + (yMath/abs(yMath))
        if tail < 8:
            moveSegment(tail+1, Tpos[tail], next)
        else:
            stops[str(Tpos[8][0])+"-"+str(Tpos[8][1])] = "h"

    elif abs(yMath) >1 or abs(xMath) > 1:
        Tpos[tail][0] = Tpos[tail][0]+(math.ceil(yMath/2))
        Tpos[tail][1] = Tpos[tail][1] +(math.ceil(xMath/2))
        if tail < 8:
            moveSegment(tail+1, Tpos[tail], next)
        else:
            stops[str(Tpos[8][0])+"-"+str(Tpos[8][1])] = "h"

stops[str(Tpos[8][0])+"-"+str(Tpos[8][1])] = "h"
for line in f:
    command = line.split(" ")
    
    if command[0] == "U":
        for i in range(int(command[1])):
            Hpos[0]+=1
            if (Hpos[0] - Tpos[0][0]) >1:
                moveSegment(0, copy.deepcopy(Hpos), [1,0])
            #stops[str(Tpos[8][0])+"-"+str(Tpos[8][1])] = "y"
    if command[0] == "D":
        for i in range(int(command[1])):
            Hpos[0]+=-1
            if (Tpos[0][0] - Hpos[0]) >1:
                moveSegment(0, copy.deepcopy(Hpos), [-1,0])
            #stops[str(Tpos[8][0])+"-"+str(Tpos[8][1])] = "y"
    if command[0] == "R":
        for i in range(int(command[1])):
            Hpos[1]+=1
            if (Hpos[1] - Tpos[0][1]) >1:
                moveSegment(0, copy.deepcopy(Hpos), [0,1])
            #stops[str(Tpos[8][0])+"-"+str(Tpos[8][1])] = "y"
    if command[0] == "L":
        for i in range(int(command[1])):

            Hpos[1]+=-1
            if (Tpos[0][1] - Hpos[1]) >1:
                moveSegment(0, copy.deepcopy(Hpos), [0,-1])
            #stops[str(Tpos[8][0])+"-"+str(Tpos[8][1])] = "y"


stops[str(Tpos[8][0])+"-"+str(Tpos[8][1])] = "y"
print(len(stops))
#36