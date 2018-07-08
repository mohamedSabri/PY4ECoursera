# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
content = fh.read()
content = content.upper()
print(content)
Use words.txt as the file name


# solution to make the program run in the auto grader use rstrip() or strip()

# fname = input("Enter file name: ")
# fh = open(fname)
# content = fh.read()
# print(content.rstrip().upper())
