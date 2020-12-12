import re
correctBags = []

def count_bags(color):
    for l in lines:
        match = re.search('(.*) bags contain .*' + color, l)
        if match:
            print(match.group(1))
            if match.group(1) not in correctBags:
                correctBags.append(match.group(1))
            count_bags(match.group(1))

f = open("input.txt")
lines = [l.strip() for l in f.readlines()]

count_bags('shiny gold')

print(len(correctBags))