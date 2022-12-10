f = open("input.txt", "r")
print("hello")

answer = 0
items = []
priority = {}

for num in range(26):
    priority[chr(num+97)] = num+1

for num in range(26):
    priority[chr(num+65)] = num+27

#print(priority)
for line in f:
    half = (len(line))//2
    firstHalf = line[0:half]
    secHalf = line[half:]
    for letter in line:
        if secHalf.find(letter) >= 0:
            items.append(letter)
            break

for item in items:
    plus = priority[item]
    answer = answer + priority[item]
    #print(str(answer)+" "+ item + " "+str(plus))
print(items)
#print(len(items))

print(answer)
