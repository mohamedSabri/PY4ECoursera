counts = dict()
print("Enter a line of text:")
line = input('')
words = line.split()
print("words:",words)

print("Counting ......... ")
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)

for key in counts:
    print(key,counts[key])

# using keys(),values(),items() methods
dictionary = dict()
dictionary['mohamed'] = 1
dictionary['ali'] = 2
dictionary['ahmed'] = 5
print(dictionary)

print(list(dictionary))
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
