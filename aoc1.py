f = open("input.txt", "r")
n = f.readlines()

for line in n:
    for line2 in n:
        for line3 in n:
            if int(line) + int(line2) + int(line3) == 2020:
                print(int(line)*int(line2)*int(line3))


    



    
        
    
