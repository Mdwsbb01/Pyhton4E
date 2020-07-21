#EX1:Exercise 1: Revise a previous program as follows:
# Read and parse the “From” lines and pull out the addresses from the line.
# Count the number of messages from each person using a dictionary.
# After all the data has been read,
# print the person with the most commits
# by creating a list of (count, email) tuples from the dictionary.
# Then sort the list in reverse order and print out the person
# who has the most commits.
'''
prompt = 'Enter the file name: '
fname = input(prompt)
fhand = open(fname)
count = dict()
count2 = dict()
lst = list()
for line in fhand:
    if line.startswith('From'):
        emailadd = line.rstrip().split()[1]
        for x in [emailadd]:
            count[x] = count.get(x, 0) + 1
            for key, value in count.items():
                new_tup = (value, key)
                lst.append(new_tup)
            lst = sorted(lst, reverse=True)
            for value, key in lst:
                continue
print(lst[0][1], lst[0][0])
'''
#EX2:This program counts the distribution of the hour
# of the day for each of the messages.
# You can pull the hour from the “From” line
# by finding the time string and then splitting
# that string into parts using the colon character.
# Once you have accumulated the counts for each hour,
# print out the counts, one per line, sorted by hour as shown below.
'''
prompt = 'Enter the file name: '
fname = input(prompt)
count = dict()

try:
    fhand = open(fname)
except:
    print('Invalid file name')
for line in fhand:
    if line.startswith('From') and not line.startswith('From:'):
        div = line.rstrip().split(':')
        hour = [div[0].split()[-1]]
        for x in hour:
            count[x] = count.get(x, 0) + 1
for key, value in sorted(count.items()):
    print(key, value)
'''
#Answer in stackoverflow
'''
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours = dict()
for line in handle:
   if line.startswith("From "):
    hour = line.split()[5].split(':')[0] 
    hours[hour] = hours.get(hour, 0) + 1
for key, value in sorted(hours.items(), None):
    print key, value
'''
#Exercise 3: Write a program that reads a file and prints the
# letters in decreasing order of frequency.
# Your program should convert all the input to
# lower case and only count the letters a-z.
# Your program should not count spaces, digits,
# punctuation, or anything other than the letters a-z.
# Find text samples from several different languages
# and see how letter frequency varies between languages.
# Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

prompt = 'Enter the file name: '
fname = input(prompt)
fhand = open(fname)
no_digits = list()
for line in fhand:
    first_move = line.rstrip().split()


#难点在于如何处理数据，让其只有a-z