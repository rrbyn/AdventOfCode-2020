f = open("input.txt", "r")
#n = f.readlines()
lettersList = []
allLetters = ""
linesList = []
counter = 0
answerCount = 0

while f: # processing data
    line = f.readline()
    line = line.strip("\n")
    if line == "" and not lettersList:
        break
    if line != "":
        linesList.append(line)
        for letter in line:
            allLetters += letter
            if letter not in lettersList:
                lettersList.append(letter)

    else: #when data is processed:
        for x in lettersList:
            if allLetters.count(x) == len(linesList):
                answerCount += 1
        

        linesList = [] #resets
        lettersList = []
        allLetters = ""

print(answerCount)
    

