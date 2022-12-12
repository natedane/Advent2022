import re
f = open("input.txt", "r")
print("hello day 4")
#81-88,29-80
answer = 0
for line in f:
    sep = re.split(",|-|\\n", line)
    if int(sep[0]) > int(sep[2]):
        temp = [sep[2], sep[3], sep[0], sep[1]]
        sep = temp
    m = (int(sep[0]) - int(sep[2])) * (int(sep[1]) - int(sep[3]))
    if m <= 0:
        answer += 1
        print("inc1 "+line)
    elif int(sep[1]) >= int(sep[2]) and int(sep[3]) >= int(sep[1]):
        answer += 1
        print("inc2 "+line)




print(answer)
