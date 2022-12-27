import re
f = open("test.txt", "r")
print("hello day 20")

original = []
keyArray = {}
i = -1


for line in f:
    i+=1
    keyArray[str(int(line))+"-"+str(i)] = i
    original.append(int(line))
print(keyArray)
for order in range(0,i):
    moving = original[order]
    print(moving)
    if moving > 1:
        keyArray[str(moving)+"-"+str(order)]+=int(moving)

print(keyArray)