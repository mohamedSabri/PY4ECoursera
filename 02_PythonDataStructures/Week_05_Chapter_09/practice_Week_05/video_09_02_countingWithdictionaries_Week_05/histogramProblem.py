dictionary = dict()
dictionary['mohamed']=1
dictionary['ali']=1
print(dictionary)
dictionary['mohamed']=dictionary['mohamed']+1
print(dictionary)

'''
# Histogram problem counting names using in and if,else
counts = dict()
names = ['mohamed','ali','ahmed','mohamed']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name]+1
print(counts)
'''
# Histogram problem Simplified Counting with get()
counts = dict()
names = ['mohamed','ali','ahmed','mohamed']
for name in names:
    counts[name] = counts.get(name,0)+1
print(counts)
