f = open("input.txt", "r")
n = f.readlines()
#print(n)
validpasswordCount = 0
#counter = 0

for line in n:
    #counter = 0
    letterPos1 = int(line.split(": ")[0].split(" ")[0].split("-")[0])
    letterPos2 = int(line.split(": ")[0].split(" ")[0].split("-")[1])
    correctLetter = line.split(": ")[0].split(" ")[1]
    password = line.split(": ")[1]
    #print(letterPos1, letterPos2, correctLetter)

    if (correctLetter == password[(letterPos1 - 1)]) and (correctLetter != password[(letterPos2 - 1)]) or (correctLetter != password[(letterPos1 - 1)]) and (correctLetter == password[(letterPos2 - 1)]):
        validpasswordCount += 1

print(validpasswordCount)
            
            