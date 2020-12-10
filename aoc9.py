f = open("input.txt", "r")
n = f.readlines()
preamble = 25
correctnr = []
lines = [l.strip() for l in n]

for el in lines[preamble:]:
    for x in lines[(preamble - 25):preamble]:
        for y in lines[(preamble - 25):preamble]:
            if int(el) - int(x) - int(y) == 0 and el not in correctnr and x != y:
                correctnr.append(el)
    preamble += 1


for el in lines[25:]:
    if el not in correctnr:
        print(el)
