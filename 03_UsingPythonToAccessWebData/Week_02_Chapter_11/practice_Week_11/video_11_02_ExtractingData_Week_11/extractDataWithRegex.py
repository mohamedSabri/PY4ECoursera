import re

x = 'My g favorite numbers are gg and g AI UO'
 # find any one or more digit (use range)
y = re.findall('[0-9]+',x)

# find any one or more sub string that is A,I,O,E,U or any combination of them (use listing the required characters)
# this will match AI,EU,AIO,UO,AIO,...
g = re.findall('[AIOEU]+',x)
# print(y)
print(g)

# greedy matching
s = 'From: Using the : character'
regex = '^F.+?:'
greedy_matching = re.findall(regex,s)
print(greedy_matching)

mail = 'mohamed@gmail'
greedy_regex_mail = '\S+@\S+'
greedy_matching_mail = re.findall(greedy_regex_mail,mail)
print(greedy_matching_mail)

non_greedy_regex_mail = '\S+?@\S+?'
non_greedy_matching_mail = re.findall(non_greedy_regex_mail,mail)
print(non_greedy_matching_mail)

#----------------------------------------
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2088'

# \S => [^ ]

regex_data_plus = '@([^ ]+)'
regex_data_asterisk = '@([^ ]*)'

'''
    if data look like this 'stephen.marquard@ uct.ac.za' has space after @ sign
    then the regex that uses asterisk will not match and return a list that contains empty string ['']
    but the regex that uses plus will match and return an empty list[]

    print('size:'+str(len(re.findall(regex_data_plus,data)))) # 0
    print('size:'+str(len(re.findall(regex_data_asterisk,data)))) # 1
'''
print(re.findall(regex_data_plus,data))
print(re.findall(regex_data_asterisk,data))

#------ Escape Character

cookies = 'we just recieve $10.00 for cookies'
regex_cookies = '\$[0-9.]+'
cookies_price = re.findall(regex_cookies,cookies)
# if you want to extract just the price use regex_cookies = '\$([0-9.]+)'
print(cookies_price)
