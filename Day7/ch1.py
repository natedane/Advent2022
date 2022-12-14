import re
f = open("input.txt", "r")
print("hello day 7")
dirs = {}
answer = ""
ad = []
current = ""
parent = ""

def addUp(current, size):
    #print(current)
    dirs[current]["size"]+=size
    if current != "//":
        addUp(dirs[current]["parent"],size)
    return


for line in f:
    #print(line)
    if line[0] == "$":
        command = line.split(" ")
        if command[1] == "cd":
            if command[2][0:2] == "..":
                #print(dirs[current])
                current = dirs[current]['parent']
                continue
            else:
                parent = current
                if current == "/":
                    current ="/"
                else:
                    current = parent+"/"+command[2][0:-1]
                if current not in dirs.keys():
                    dirs[current] = {"dir":[], "size":0, "parent":parent}
                    #print(str(dirs))
        if command[1] == "ls":
            continue
        
    elif line[0:3] == "dir":
        command = line.split(" ")
        dirs[current]["dir"].append(command[1][0:-1])
    else:
        command = line.split(" ")
        dirs[current]["size"]+= int(command[0])
        addUp(dirs[current]["parent"],int(command[0]))

space = 70000000 - dirs["//"]["size"]
space = 30000000 - space
print(space)
min = 70000000

for key in dirs.keys():
    #print(dirs[key])
    if dirs[key]["size"] > space and dirs[key]["size"]<min:
        answer = key
        min = dirs[key]["size"]
        ad.append(key)
        #print(str(dirs[key]["size"])+ " "+ key)
#print(dirs)
print(answer)
print(min)
print(ad)