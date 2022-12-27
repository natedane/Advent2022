import re
f = open("input.txt", "r")
print("hello day 8")
trees = []

answer = ""
i = 0

for line in f:
    trees.append([])
    for t in line:
        if t == "\n":
            continue
        trees[i].append(t)
    i += 1

treeRow = len(trees[0])
treeCol= len(trees)
#top down
treeKey = {}
for row in range(treeCol):
    tallest = -1
    for col in range(treeRow):
        print(str(tallest)+" min for "+ str(trees[col][row]))
        if tallest < int(trees[col][row]):
            tallest = int(trees[col][row])
            treeKey[str(col)+"-" +str(row)] = "up"+trees[col][row]
        if tallest == 9:
            break

#down up
for row in range(treeCol-1,-1,-1):
    tallest = -1
    for col in range(treeRow-1,-1,-1):
        print(str(tallest)+" min for "+ str(trees[col][row]))
        if tallest < int(trees[col][row]):
            tallest = int(trees[col][row])
            treeKey[str(col)+"-" +str(row)] = "down"+trees[col][row]
        if tallest == 9:
            break

#left to right
for col in range(treeRow):
    tallest = -1
    for row in range(treeCol):
        print(str(tallest)+" min for "+ str(trees[col][row]))
        if tallest < int(trees[col][row]):
            tallest = int(trees[col][row])
            treeKey[str(col)+"-" +str(row)] = "left"+trees[col][row]
        if tallest == 9:
            break

#right to left
for col in range(treeRow-1,-1,-1):
    tallest = -1
    for row in range(treeCol-1,-1,-1):
        print(str(tallest)+" min for "+ str(trees[col][row]))
        if tallest < int(trees[col][row]):
            tallest = int(trees[col][row])
            treeKey[str(col)+"-" +str(row)] = "right"+trees[col][row]
        if tallest == 9:
            break


print(treeKey)
print(len(treeKey))
