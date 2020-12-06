f = open("input.txt", "r")
n = f.readlines()
n = [x.replace('\n', '') for x in n]
#print(n)
xCounter = 0
yCounter = 0
answerCounter = 0
loopTimes = 1
start = 0



for line in n:
    if (yCounter != len(n)-1):
        xCounter += 1
        yCounter += 2
        if xCounter + 3 > len(line):
            for line in n:
                n[start] += line
                #print (n[start])
                start += 1
                if start == len(n):
                    start = 0
                    break
                
                
        currentPos = n[yCounter][xCounter]
        print(n[yCounter])
        #print(currentPos)
        if (currentPos == "#"):
            answerCounter += 1
            print("X", yCounter, answerCounter)
        else:
            print("O", yCounter, answerCounter)
print(answerCounter)


