import re
f = open("input.txt", "r")
print("hello day 8")
trees = []


i = 0

for line in f:
    trees.append([])
    for t in line:
        if t == "\n":
            continue
        trees[i].append(t)
    i += 1

def traverse(treeCol, treeRow):
    tall = int(trees[treeCol][treeRow])
    #print("starting "+str(tall))
    dirs = [0,0,0,0]
    if treeCol==0 or treeRow ==0 or treeCol == len(trees) or treeRow == len(trees[0]):
        return 0
    #left
    for row in range(treeRow-1,-1,-1):
        #print(str(tall) +" l " +trees[treeCol][row])
        dirs[0] +=1
        if tall <= int(trees[treeCol][row]):
            break
    #down
    for col in range(treeCol+1,len(trees[treeCol])):
        #print(str(tall) +" d " +trees[col][treeRow])
        dirs[1] +=1
        if tall <= int(trees[col][treeRow]):
            break
    
    #right
    for row in range(treeRow+1,len(trees[treeRow])):
        #print(str(tall) +" r " +trees[treeCol][row])
        dirs[2] +=1
        if tall <= int(trees[treeCol][row]):
            break

    #up
    for col in range(treeCol-1,-1,-1):
        #print(str(tall) +" u " +trees[col][treeRow])
        dirs[3] +=1
        if tall <= int(trees[col][treeRow]):
            break

    #print(dirs)
    return(dirs[0]*dirs[1]*dirs[2]*dirs[3])
        

treeRow = len(trees[0])
treeCol= len(trees)
answer = 0
#top down

for row in range(treeCol):
    for col in range(treeRow):
        max = traverse(col,row)
        #print(max)
        if max > answer:
            answer = max


print(answer)
