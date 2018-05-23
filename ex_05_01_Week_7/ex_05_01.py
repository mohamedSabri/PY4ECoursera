total = 0
count=0
average =0
while True:
    input_string = input("Enter a number: ")
    if input_string == 'done':
        break
    try:
        number = float(input_string)
    except:
        print('Invalid input')
        continue
    count +=1
    total += number

if count != 0:
    average=total/count
print('total:',total,'count:',count,'average:',average)
