import re
listofbags = []

def count_bags(color, nrOfCorrectBags, bagsToProcess, bagAmount):
    for l in lines:
        match = re.search(color + ' bags contain (.*)', l)
        if match:
            if match.group(1) == "no other bags.":
                bagsToProcess.pop(0)
                if len(bagsToProcess) == 0:
                    return [nrOfCorrectBags]
                color = bagsToProcess[0][-2] + " " + bagsToProcess[0][-1]
                bagAmount = bagsToProcess[0][0]
            else:
                bags = match.group(1).split(",")  
                for bag in bags:
                    bag = bag.strip().split(" ")
                    bag.pop(-1)
                    nrOfCorrectBags += int(bag[0]) * int(bagsToProcess[0][0])
                    print(nrOfCorrectBags)
                    bagsToProcess.append(bag)
                bagsToProcess.pop(0)
                color = bagsToProcess[0][-2] + " " + bagsToProcess[0][-1]
                bagAmount = bagsToProcess[0][0]
    return count_bags(color, nrOfCorrectBags, bagsToProcess, bagAmount)
            
            

f = open("input.txt")
lines = [l.strip() for l in f.readlines()]
count_bags('shiny gold', 0, [["1","shiny","gold"]], 1)

