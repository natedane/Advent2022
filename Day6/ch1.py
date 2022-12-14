import re
f = open("input.txt", "r")
print("hello day 4")

buffer = []
found = 0
answer = 0

def check(buffer):
    print(buffer)
    #for i in range(len(buffer) -1):
    for i in range(len(buffer) -2,-1,-1):
        if buffer[len(buffer)-1] == buffer[i]:
            return max(i+1,found-1)
    return max(found -1,0)

answer = 0
for line in f:
    for letter in line:
        buffer.append(letter)
        answer +=1
        
        found = check(buffer)
        print(found)
        if found == 0 and len(buffer)==14:
          break
        if len(buffer) == 14:
            buffer = buffer[1:14]
        



print(buffer)
print(answer)