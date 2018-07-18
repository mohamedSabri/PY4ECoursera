import re

file_name = input('Enter File name:')
file_hand = open(file_name)

sum = 0
regex = '[0-9]+'

for line in file_hand:
    line = line.rstrip()
    stuff = re.findall(regex,line)
    if stuff:
        for i in stuff:
            sum += int(i)
print("sum",sum)
