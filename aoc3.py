f = open("input.txt", "r")
n = f.readlines()
n = [x.replace('\n', '') for x in n]
xCoordinate = 0
yCoordinate = 0
answerCounter = 0
start = 0

for line in n:
    if (yCoordinate != len(n)-1):
        xCoordinate += 1
        yCoordinate += 2
        if xCoordinate + 3 > len(line):
            for line in n:
                n[start] += line
                start += 1
                if start == len(n):
                    start = 0
                    break             
                
        currentPos = n[yCoordinate][xCoordinate]
        if (currentPos == "#"):
            answerCounter += 1
            
print(answerCounter)


