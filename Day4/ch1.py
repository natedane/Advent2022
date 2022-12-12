import re
f = open("input.txt", "r")
print("hello day 4")

answer = 0
for line in f:
    sep = re.split(",|-|\\n", line)
    m = (int(sep[0]) - int(sep[2])) * (int(sep[1]) - int(sep[3]))
    if m <= 0:
        answer += 1
        print("inc")
    print(line)



print(answer)
