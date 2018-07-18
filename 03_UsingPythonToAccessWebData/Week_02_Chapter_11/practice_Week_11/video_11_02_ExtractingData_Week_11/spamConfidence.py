import re

fhand = open("mbox-short.txt")
numList = list()
regex = '^X-DSPAM-Confidence: ([0-9.]+)'
for line in fhand:
    line = line.rstrip()
    stuff = re.findall(regex,line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numList.append(num)

print('Maximum:',max(numList))
