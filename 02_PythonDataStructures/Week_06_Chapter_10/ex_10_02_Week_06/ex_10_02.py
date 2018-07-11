file_name = input("Enter File Name:")
if len(file_name) < 1: file_name = "mbox-short.txt"
file_handle = open(file_name, "r")

sending_time_index = 5
sending_hours_dictionary = dict()

for line in file_handle:
    if not line.startswith("From "):
        continue
    sending_time = line.split()[sending_time_index]
    sending_hour = sending_time.split(":")[0]
    sending_hours_dictionary[sending_hour] = sending_hours_dictionary.get(sending_hour,0) + 1
'''
    using sorted method 
'''
for k, v in sorted(sending_hours_dictionary.items()):
    print(k, v)

'''
    you can sort using sort method for lists.
'''

# sending_hours_list = sending_hours_dictionary.items()
# sending_hours_list.sort()
# for k , v in sending_hours_list:
#     print(k,v)


'''
    ** What is the difference between `sorted(list)` vs `list.sort()`? **

    sorted() returns a new sorted list, leaving the original list unaffected.
    list.sort() sorts the list in-place, mutating the list indices, and returns None (like all in-place operations).

    sorted() works on any iterable,not just lists. Strings,tuples,dictionaries(you'll get the keys), generators, etc.
    returning a list containing all elements, sorted.

    Use list.sort() when you want to mutate the list, sorted() when you want a new sorted object back.
    Use sorted() when you want to sort something that is an iterable, not a list yet.

    For lists, list.sort() is faster than sorted() because it doesn't have to create a copy.
    For any other iterable, you have no choice.

    you cannot retrieve the original positions. Once you called list.sort() the original order is gone.

    REF: https://stackoverflow.com/questions/22442378/what-is-the-difference-between-sortedlist-vs-list-sort
'''
