#Exercise 2:
# Write a program that categorizes each mail messag
# by which day of the week the commit was done.
# To do this look for lines that start with “From”,
# then look for the third word and keep a running count
# of each of the days of the week.
# At the end of the program print out the contents of
# your dictionary (order does not matter).
'''
prompt = 'Enter the file name: '
fname = input(prompt)
fhand = open(fname)
counts = dict()

for line in fhand:
    if line.startswith('From') and not line.startswith('From:'):
        line = line.rstrip().split()
        day = line[2]
        days = [day]
        for x in days:
            if x not in counts:
                counts[x] = 1
            else:
                counts[x] = counts[x] + 1
        #for x in days:
            #counts[x] = counts.get(x, 0) + 1
print(counts)
'''
'''
#Exercise 3: Write a program to read through a mail log,
# build a histogram using a dictionary to count
# how many messages have come from each email address,
# and print the dictionary.

prompt = 'Enter the file name: '
fname = input(prompt)
fhand = open(fname)
count = dict()
for line in fhand:
    if line.startswith('From'):
        line = line.rstrip().split()
        emailadd = line[1]
        address = [emailadd]
        for x in address:
            count[x] = count.get(x, 0) + 1
print(count)
'''
'''
#ex4:Add code to the above program to figure out
# who has the most messages in the file.
# After all the data has been read
# and the dictionary has been created,
# look through the dictionary
# using a maximum loop (see Chapter 5: Maximum and minimum loops)
# to find who has the most messages and
# print how many messages the person has.
prompt = 'Enter the file name: '
fname = input(prompt)
fhand = open(fname)
count = dict()
bigcount = None
bigadd = None
for line in fhand:
    if line.startswith('From'):
        line = line.rstrip().split()
        emailadd = line[1]
        address = [emailadd]
        for x in address:
            count[x] = count.get(x, 0) + 1
for k, v in count.items():
    if bigcount is None or v > bigcount:
        bigcount = v
        bigadd = k
print(bigadd, bigcount)
'''
#Exercise 5: This program records the domain name
# (instead of the address) where the message
# was sent from instead of who the mail came from
# (i.e., the whole email address).
# At the end of the program, print out the contents
# of your dictionary.
prompt = 'Enter the file name: '
fname = input(prompt)
fhand = open(fname)
count = dict()
for line in fhand:
    if line.startswith('From'):
        email = line.rstrip().split()[1]
        emailadd = [email.split('@')[1]]

        for x in emailadd:
            count[x] = count.get(x, 0) + 1
print(count)


