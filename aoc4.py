f = open("input.txt", "r")
counter = 0
d={}
eyeColours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def hairChecker(code):
    counter = 0
    for x in code:
        if x.isnumeric():
            if (int(x) <= 9 and int(x) >= 0) :
                counter += 1
        elif x.isalpha():
            if (str(x) <= 'f' and str(x) >= 'a'):
                counter += 1
    if counter == 5:
        return True
    else:
        return False



while f:
    line = f.readline()
    if line == "" and not d:
        break
    dictMaker = line.split(" ")
    if line != "\n" and line != "":
        for el in dictMaker:
            el = el.split(":")
            d[el[0]] = el[1].strip("\n")
    else:
        if 'byr' in d.keys() and int(d['byr']) >= 1920 and int(d['byr']) <= 2002:
            if 'pid' in d.keys() and len(d['pid']) == 9:
                if 'eyr' in d.keys() and int(d['eyr']) >= 2020 and int(d['eyr']) <= 2030:
                    if 'hcl' in d.keys() and (d['hcl'][0] == "#") and len(d['hcl']) == 7 and hairChecker(d['hcl'][1:-1]) == True:
                        if 'ecl' in d.keys() and d['ecl'] in eyeColours:
                            if 'iyr' in d.keys() and int(d['iyr']) >= 2010 and int(d['iyr']) <= 2020:
                                if 'hgt' in d.keys():
                                    if d['hgt'][-2:] == "cm" or d['hgt'][-2:] == "in":
                                        if (d['hgt'][-2:] == "cm"):
                                            if int(d['hgt'][:-2]) >= 150 and int(d['hgt'][:-2]) <= 193:
                                                print(d.keys())
                                                print('is valid')
                                                counter += 1
                                        else:
                                            if int(d['hgt'][:-2]) >= 59 and int(d['hgt'][:-2]) <= 76:
                                                print(d.keys())
                                                print('is valid')
                                                counter += 1
        
        d={}
    
print(counter)

