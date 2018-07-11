fileName = input("Enter File Name:")
fileHandle = open(fileName)

dictionary = dict()

for line in fileHandle:
    words = line.split()
    if words: # if words != []
        for word in words:
            # idiom: retrieve/create/update counter
            dictionary[word] = dictionary.get(word,0) + 1

# find the 10 top most common words
'''
    we should get the dictionary.items() List of tuples result
    and reverse it with value, key then sort it Desc and print the first 10 tuples
'''

reverseList = list()
for key,value in dictionary.items():
    reverseList.append((value,key))
# sort the list from big value to small value
reverseList = sorted(reverseList,reverse = True)
# you should reverse the key value in the for because it reversed in the list,but type them in order for print
for value,key in reverseList[:10]:
    print(key,value)
print(" ----------------------------------------------------------- ")
# Using List Comprehension to get the same result in less code
reverseList = sorted([(v,k) for k,v in dictionary.items()],reverse=True)
for value,key in reverseList[:10]:
    print(key,value)
