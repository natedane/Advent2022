import re
f = open("test.txt", "r")
print("hello day 10")
message = [""]
answer = []
clock = 0
x = 1
buffer = 0
clockCheck = [20,60,100,140,180]
earlyCheck = [19,59,99,139,179,219]

def writeConsole():
    position = int(clock %40)
    window = position - x

    print(str(clock)+" "+line+ str(x) + message[0])
    if position == 0:
        message[0] += "\n"
    if abs(window) < 3:
        message[0] += " # "
    else:
        message[0] += " . "
i = -1
# writeConsole()
# clock +=1
for line in f:
    i+=1
    if(i == 20):
        break
    if line[0:3] == "add":
        if clock in earlyCheck:
            print(str(clock)+" "+str(x))
            answer.append(x*(clock+1))
        if clock in clockCheck:
            print(str(clock)+" "+str(x))
            answer.append(x*(clock))
        command = line.split(" ")
        #writeConsole()
        clock +=1
        writeConsole()
        buffer = (int(command[1]))
    elif clock in clockCheck:
        print(str(clock)+" "+str(x))
        answer.append(x*clock)
    
    clock +=1
    writeConsole()
    x +=buffer
    buffer = 0
   
print(answer)
print(sum(answer))
print(message)