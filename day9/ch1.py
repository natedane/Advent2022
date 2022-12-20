import re
f = open("input.txt", "r")
print("hello day 9")

Hpos = [0,0]
Tpos = [0,0]
stops = {}

for line in f:
    command = line.split(" ")
    #print(command)
    if command[0] == "U":
        for i in range(int(command[1])):
            Hpos[0]+=1
            if (Hpos[0] - Tpos[0]) >1:
                stops[str(Tpos[0])+"-"+str(Tpos[1])] = "h"
                Tpos[0] = Hpos[0]-1
                Tpos[1] = Hpos[1]
    if command[0] == "D":
        for i in range(int(command[1])):
            Hpos[0]+=-1
            if (Tpos[0] - Hpos[0]) >1:
                stops[str(Tpos[0])+"-"+str(Tpos[1])] = "h"
                Tpos[0] = Hpos[0]+1
                Tpos[1] = Hpos[1]
    if command[0] == "R":
        for i in range(int(command[1])):
            Hpos[1]+=1
            if (Hpos[1] - Tpos[1]) >1:
                stops[str(Tpos[0])+"-"+str(Tpos[1])] = "h"
                Tpos[0] = Hpos[0]
                Tpos[1] = Hpos[1]-1
    if command[0] == "L":
        for i in range(int(command[1])):
            Hpos[1]+=-1
            if (Tpos[1] - Hpos[1]) >1:
                stops[str(Tpos[0])+"-"+str(Tpos[1])] = "y"
                Tpos[0] = Hpos[0]
                Tpos[1] = Hpos[1]+1
                print(str(Tpos)+" added")
            print(str(Hpos)+" h")
            print(Tpos)
stops[str(Tpos[0])+"-"+str(Tpos[1])] = "y"
print(stops)
print(len(stops))