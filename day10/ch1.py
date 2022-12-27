import re
f = open("input.txt", "r")
print("hello day 10")

answer = []
clock = 0
x = 1
#buffer = []
clockCheck = [20,60,100,140,180]
earlyCheck = [19,59,99,139,179,219]


for line in f:
    clock +=1
    if line[0:3] == "add":
        if clock in earlyCheck:
            print(str(clock)+" "+str(x))
            answer.append(x*(clock+1))
        if clock in clockCheck:
            print(str(clock)+" "+str(x))
            answer.append(x*(clock))
        command = line.split(" ")
        clock +=1
        x += int(command[1])
        #buffer.append(int(command[1]))
    elif clock in clockCheck:
        print(str(clock)+" "+str(x))
        answer.append(x*clock)
   
print(answer)
print(sum(answer))