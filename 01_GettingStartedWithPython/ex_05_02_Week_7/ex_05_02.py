largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    #print(num)
    try:
        integer_Value = int(num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest = integer_Value
    elif largest < integer_Value :
        largest = integer_Value
    if smallest is None:
        smallest = integer_Value
    elif smallest > integer_Value :
        smallest = integer_Value 

print("Maximum is", largest)
print("Minimum is",smallest)
