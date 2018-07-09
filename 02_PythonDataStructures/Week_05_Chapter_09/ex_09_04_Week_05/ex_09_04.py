file_name = input('Enter File Name:')
if len(file_name) < 1 : file_name = "mbox-short.txt"

file_handle = open(file_name)

sender = dict()

for line in file_handle :
    if line.startswith('From '):
        words = line.split()
        sender[words[1]] = sender.get(words[1],0) + 1

greatest_sender_value = None
greatest_sender_key = None

for key,value in sender.items():
    if greatest_sender_key is None or greatest_sender_value < value:
        greatest_sender_value = value
        greatest_sender_key = key
print(greatest_sender_key,greatest_sender_value)
