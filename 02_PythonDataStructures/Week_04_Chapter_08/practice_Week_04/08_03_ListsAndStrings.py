fhand = open('mbox-short.txt')
for line in fhand:
    line= line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print("This e-mail has been sent at " + words[2])
    # get the domain for each mail
    email = words[1]
    email_words = email.split('@')
    domain = email_words[1]
    print ("email:" + email + " its domain:" + domain)
