sum = 0
count = 0
print('Before',count,sum)
for value in  [9,41,12,3,74,15]:
    count +=1
    sum += value
    print(count,sum,value)
average = sum/count
print('After',count,sum,average)
