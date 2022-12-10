f = open("input.txt", "r")
print("hello")

answer = 0
items = []
priority = {}
round = []

for num in range(26):
    priority[chr(num+97)] = num+1

for num in range(26):
    priority[chr(num+65)] = num+27

#print(priority)
for line in f:
    round.append(line)
    if len(round) > 2:
        for letter in round[0]:
            if round[1].find(letter) >= 0 and round[2].find(letter) >= 0:
                items.append(letter)
                print("found "+letter+round[0])
                break
        round.clear()
        #print("clear")
        #print(str(len(round)))

print(items)
for item in items:
    plus = priority[item]
    answer = answer + priority[item]
    #print(str(answer)+" "+ item + " "+str(plus))

print(len(items))

print(answer)
