fname = input("Enter file name: ")
if len(fname) < 1:fname = "mbox-short.txt"

fhand = open(fname)
count = 0
for line in fhand:
    if not line.startswith("From "): continue
    count += 1
    line = line.rstrip()
    words = line.split()
    print (words[1])


print("There were", count, "lines in the file with From as the first word")
