#A X rock
#B Y paper
#C Z scissors

f = open("input.txt", "r")
score = 0;

key = {"AX": 3, "BY":5, "CZ":7, "AY":4, "AZ":8, "BX":1, "BZ":9, "CX":2, "CY":6}

for line in f:
    combo = line[0]+line[2]
    #print(combo+ str(key.get(combo)))
    score +=key.get(combo)

print(score)
#15702
