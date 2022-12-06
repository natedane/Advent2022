#A X rock
#B Y paper
#C Z scissors

f = open("input.txt", "r")
score = 0;

key = {"AX": 4, "BY":5, "CZ":6, "AY":8, "AZ":3, "BX":1, "BZ":9, "CX":7, "CY":2}

for line in f:
    combo = line[0]+line[2]
    #print(combo+ str(key.get(combo)))
    score +=key.get(combo)

print(score)
#15523
