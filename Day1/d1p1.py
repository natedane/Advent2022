f = open("input.txt", "r")
print("hello")

highest = 0
elf = 0

for line in f:
    if line == "\n":
        if elf > highest:
            highest = elf
        elf = 0
    else:
        elf += int(line)



print(highest)
