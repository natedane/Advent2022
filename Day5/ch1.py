import re
f = open("input.txt", "r")
print("hello day 5")
boxes = []
i=0
answer = ""

def initBoxes(size):
    stacks = int((size)/4)
    for s in range(stacks):
        boxes.append([])
    

def moveStack(line):
    sep = re.split(" ", line)
    move = int(sep[1])
    f = int(sep[3])-1
    to = int(sep[5])-1
    for a in range(move):
        boxes[to].append(boxes[f].pop())

    

for line in f:
    if len(boxes) == 0:
        initBoxes(len(line))
        #print(boxes)
    if line[0:2] == " 1":
        for stack in range(len(boxes)):
            boxes[stack].reverse()
            print("reverse ")
    if line.find("[")>=0:
        for position in range(1,len(line),4):
            #print(str(position)+" of " + str(len(line))+ " "+ line[position])
            if line[position] != " ":
                boxes[i].append(line[position])
            i += 1
        i=0
        
    if line.find("move") >=0:
        print(boxes)
        print(line)
        print(boxes)
        moveStack(line)



print(boxes)
for i in  range(len(boxes)):
    answer += boxes[i].pop()
print(answer)
print("done")



