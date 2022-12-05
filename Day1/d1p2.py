f = open("input.txt", "r")
print("hello")

highest = [0,0,0]
elf = 0

for line in f:
    if line == "\n":
        if elf > highest[0]:
            highest[0] = elf
            highest.sort()
        elf = 0
    else:
        elf += int(line)
print(sum(highest))



