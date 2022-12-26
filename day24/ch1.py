import re
f = open("input.txt", "r")
print("hello day 10")

answer = 0
valley = [[]]
legend = {">":2,"<":8,"^":4,"v":1,".":0,"#":-1}
i=0
for line in f:
    valley[0].append([])
    for space in line:
        if space in legend:
            valley[0][i].append(legend[space])
    i+=1

def valleyPrint():
    for minute in valley:
        print("minute ")
        for row in minute:
            print(row)

bottom = len(valley[0])-1
right = len(valley[0][0])-2
maxMinute = 0


#1 v, 2 >, 4 ^, 8 <
def nextMinute():
    next = len(valley)
    valley.append([])
    for row in range(0,bottom+1):
        valley[next].append([])
        for col in range(0,right+2):
            valley[next][row].append(-1)
    valley[next][0][1] = 0
    for row in range(1,bottom):
        for col in range(1,right+1):
            space = valley[next-1][row][col]
            valley[next][row][col] +=1
            #print(str(row)+" "+str(col)+" space:"+str(space))
            if (space - 8)>=0:
                space -= 8
                if col == 1:
                    valley[next][row][right] +=8
                else:
                    valley[next][row][col-1] +=8
            if (space - 4)>=0:
                space -= 4
                if row == 1:
                    valley[next][bottom-1][col]+=4
                else:
                    valley[next][row-1][col]+=4
            if (space - 2)>=0:
                space -= 2
                if col == right:
                    valley[next][row][1]+=2
                else:
                    valley[next][row][col+1]+=2
            if (space - 1)>=0:
                #print(str(row)+" "+str(col)+" "+str(bottom)+" space"+ str(space))
                space -= 1
                if row == bottom-1:
                    valley[next][1][col]+=1
                else:
                    valley[next][row+1][col]+=1
            #print(str(row)+" "+str(col)+" "+str(valley[next][row][col]))

queueSearch = [[0,0,1]]
record = []

def progress(minute, position):
    #print(minute)  
    if minute >= len(valley)-1:
        nextMinute()
    if valley[minute+1][position[0]+1][position[1]] == 0:
        #print("down"+str(minute))
        next = [minute+1, position[0]+1,position[1]]
        if next not in record:
            queueSearch.append(next)
    if valley[minute+1][position[0]][position[1]+1] == 0:
        #print("right"+str(minute))
        next = [minute+1,  position[0],position[1]+1]
        if next not in record:
            queueSearch.append(next)

    if valley[minute+1][position[0]][position[1]] == 0:
        #print("wait"+str(minute))
        next = [minute+1, position[0],position[1]]
        if next not in record:
            queueSearch.append(next)

    if valley[minute+1][position[0]-1][position[1]] == 0:
        #print("up"+str(minute))
        next = [minute+1, position[0]-1,position[1]]
        if next not in record:
            queueSearch.append(next)
    if valley[minute+1][position[0]][position[1]-1] == 0:
        #print("left"+str(minute))
        next = [minute+1, position[0],position[1]-1]
        if next not in record:
            queueSearch.append(next)

    return True


while(True):
    item = queueSearch.pop(0)
    #print(item)
    if(item[1] == bottom-1 and item[2] == right):
        print("found end!!!!!!!!!!!!!!!!!!")
        answer = item[0] +1
        break
    # checkValue = item[0]*100000+item[1]*1000+item[2]
    if item in record:
        continue
    else:
        print(item)
        record.append(item)
        progress(item[0], [item[1], item[2]])
    
    

    

    if len(queueSearch) == 0:
        break



#valleyPrint()
#4, 6

print(answer)
