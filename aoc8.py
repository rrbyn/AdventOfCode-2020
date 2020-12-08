f = open("input.txt", "r")
n = f.readlines()
usedLines = []
accumulator = 0
counter = 0
currentLine = ""



while True:
    if counter != len(n):
        usedLines.append(counter)
        currentLine = n[counter]
        currentLine = currentLine.split(" ")
        currentLine[1] = currentLine[1].strip("\n")
        if counter + 2 == len(n) and currentLine[0] == "jmp":
            currentLine[0] = "nop"
        if (counter + int(currentLine[1][1:])) + 1 == len(n) and currentLine[0] == "nop":
            currentLine[0] = "jmp"
        if currentLine[0] == "nop":
            counter += 1
        elif currentLine[0] == "acc":
            if currentLine[1][0] == "+":
                accumulator += int(currentLine[1][1:])
            else:
                accumulator -= int(currentLine[1][1:])
            counter += 1
        elif currentLine[0] == "jmp":
            if currentLine[1][0] == "+":
                counter += int(currentLine[1][1:])
            else:
                counter -= int(currentLine[1][1:])
    else:
        print(accumulator)

        break
