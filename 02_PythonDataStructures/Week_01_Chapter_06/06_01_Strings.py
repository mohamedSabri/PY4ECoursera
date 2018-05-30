#Looping Through Strings
fruit = "banana"
print("print String Characters using For Loop")
for letter in fruit:
    print(letter)


index = 0
print("print String Characters using While Loop")
while index<len(fruit):
   letter = fruit[index]
   print(letter)
   index +=1

# calculate number of characters in a string

count = 0
for letter in fruit:
    count = count +1
    print(letter)
print(fruit,"has",count,"characters")

# calculate number of 'a' characters in a string
count = 0
for letter in fruit:
    if letter =="a":
    	count = count +1
print(fruit,"has",count," 'a' characters")
