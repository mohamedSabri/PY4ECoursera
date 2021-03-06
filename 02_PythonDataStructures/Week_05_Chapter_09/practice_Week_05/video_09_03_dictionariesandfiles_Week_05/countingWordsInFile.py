fileName = input("Enter File Name:")
fileHandle = open(fileName)

dictionary = dict()

for line in fileHandle:
    words = line.split()
    if words: # if words != []
        for word in words:
            # idiom: retrieve/create/update counter
            dictionary[word] = dictionary.get(word,0) + 1

# find the most common word

maxRepeatedCount = None
maxRepeatedWord = None
for key,value in dictionary.items():
    if maxRepeatedCount is None or maxRepeatedCount < value:
        maxRepeatedWord = key
        maxRepeatedCount = value

print(dictionary)
print('Max Repeated Word:' + maxRepeatedWord + ' ,Max Repeated Count:' + str(maxRepeatedCount))
