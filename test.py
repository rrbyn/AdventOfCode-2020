linesList = ["dog","dae","de"]
allLines = "dogdaede"
lettersList=["d"]
counter = 0

for x in lettersList:
    if allLines.count(x) == len(linesList):
        print('yes')