import math

f = open("input.txt", "r")
n = f.readlines()
seatIDs = []

highestID = 0


for line in n:
    maxRow = 127
    minRow = 0
    maxColumn = 7
    minColumn = 0
    for y in line[0:7]:
        if y == "F":
            maxRow = math.floor(maxRow - (maxRow - minRow)/2)
        else:
            minRow = math.ceil(minRow +(maxRow - minRow)/2)

    for x in line[7:10]:
        if x == "L":
            maxColumn = math.floor(maxColumn - (maxColumn - minColumn)/2)
        else:
            minColumn = math.ceil(minColumn +(maxColumn - minColumn)/2)

    currentID = maxRow * 8 + maxColumn
    seatIDs.append(currentID)
print(seatIDs)

for x in seatIDs:
    if x + 1 not in seatIDs:
        print(x + 1)
    


            

