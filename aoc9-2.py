f = open("input.txt", "r")
n = f.readlines()
lines = [int(l.strip()) for l in n]
answer = 0
weakness=[]
key = 10884537
l = -1

for i in range(0,len(lines)):
    for y in lines[i:]:
        loops = 0
        l += 1
        for x in lines[i+l+1:]:
            loops += 1
            y += x
            if y == key:
                for loop in range(0,loops + 1):
                    weakness.append(lines[loop + i + l])
weakness.sort()
print(weakness)
print(weakness[0],"+",weakness[-1])
answer = weakness[0] + weakness[-1]
print(answer)

                #print (lines[lines.index(x) - 1],lines[lines.index(x) - 2],lines[lines.index(x) - 3],lines[lines.index(x) - 4])



















#def finder(i,answer):
#    if answer == 127:
#        print("yes")
#        return True
#    else:
#        return lines[i + 1] + finder(answer)
#
#
#
#
#for i in range(-1,len(lines)):
#    finder(i)
