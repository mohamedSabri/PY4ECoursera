# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
lineCounter=0
average=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
         continue
    lineCounter += 1
    value = line[line.find(" ")+1:]
    value = float(value)
    average += value
    print(line)
    print("average:",average)
print("Average spam confidence:",average/lineCounter)
