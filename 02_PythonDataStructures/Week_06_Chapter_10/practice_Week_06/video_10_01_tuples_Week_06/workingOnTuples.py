(x,y) = (4,'fred')
print("x:"+str(x))
print("y:"+y)

x,y = 3,8
print("x:"+str(x))
print("y:"+str(y))

(x,y) = 'g',15
print("x:"+x)
print("y:"+str(y))

f,g = ('rrr','ggg')
print("x:"+x)
print("g:"+g)

############################################################
# sort dictionary by key
d = {'a':10, 'b':1, 'c':22}
print(d.items())
print(sorted(d.items()))

# sort dictionary by value
d = {'a':10, 'b':1, 'c':22}
tmp = list()
for v,k in d.items():
    tmp.append((k,v))
print(tmp)
# Asc
print(sorted(tmp,reverse=True))

# Desc
print(sorted(tmp,reverse=True))
