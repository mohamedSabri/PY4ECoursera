smallest = None
print('Before',smallest)
for num in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = num
    if num < smallest:
        smallest = num
    print(smallest,num)
print('After',smallest)
