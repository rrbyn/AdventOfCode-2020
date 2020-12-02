f = open("input.txt", "r")
n = f.readlines()
print(n)
validpasswordCount = 0
counter = 0

for line in n:
    counter = 0
    letterMin = int(line.split(": ")[0].split(" ")[0].split("-")[0])
    letterMax = int(line.split(": ")[0].split(" ")[0].split("-")[1])
    password = line.split(": ")[1]
    print(letterMin, letterMax)
    
    for i in password:
        if i == line.split(": ")[0].split(" ")[1]:
            counter += 1
    print(counter)
    if (counter >= letterMin) and (counter <= letterMax):
        print('yes')
        validpasswordCount += 1
    else:
        print('no')

print(validpasswordCount)
            
            