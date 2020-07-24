'''
import re
fhand = open(input('Enter the file name: '))
numlist = list()
for line in fhand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    # skip all the lines dont match
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print(max(numlist))
'''

#Exercise 1: Write a simple program to simulate
# the operation of the grep command on Unix.
# Ask the user to enter a regular expression
# and count the number of lines
# that matched the regular expression:
'''
import re
prompt1 = 'Enter the file name: '
prompt2 = 'Enter the regular expression: '
fname = input(prompt1)
fhand = open(fname)
fre = input(prompt2)
count = 0
for line in fhand:
    line = line.rstrip()
    target = re.findall(fre, line)
    if len(target) > 0:
        count = count + 1
        continue
print(fname, 'had', count, 'lines that matched', fre)
'''
#Exercise 2: Write a program to look for lines of the form
#`New Revision: 39772`
#and extract the number from each of the lines
# using a regular expression and the findall() method.
# Compute the average of the numbers
# and print out the average.
import re
prompt = 'Enter the file name: '
fname = input(prompt)
fhand = open(fname)
countlst = list()
data_dic = dict()
count = 0
for line in fhand:
    line = line.rstrip()
    data = re.findall('^New Revision: ([0-9.]+)', line)
    if len(data) > 0:
        count = count + 1
        num = float(data[0])
        countlst.append(num)
        avg = sum(countlst) / count
print(avg)
