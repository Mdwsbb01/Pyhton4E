# Exercise 1: Write a program to read
# through a file and print the contents of
# the file (line by line) all in upper case.
# Executing the program will look as follows:
'''
prompt = 'Enter the file name: '
fname = input(prompt)

fhand = open(fname)
data = fhand.read()
data = data.upper()
print(data)
'''
'''
#Exercise 2: Write a program to prompt for a file name,
# and then read through the file and look for lines of the form:

prompt = 'Enter the file name: '
fname = input(prompt)
try:
    fhand = open(fname)
except:
    print('File doesnt exist')
    quit()
count = 0
total = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence: '):
        count = count + 1
        colon = line.find(':')
        value = float(line[colon+1:])
        total = total + value
        avg = total / count
print('Average spam confidence', avg)
'''
#别人写的ex2:
'''
fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
string="X-DSPAM-Confidence:"
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else:
        count=count+1
        num=float(line[len(string)+1:]) #这里写的特别好
        total=total+num

print("Average spam confidence:",float(total/count))
'''

#EX3:  Sometimes when programmers get bored or want to have a bit of fun,
# they add a harmless Easter Egg to their program.
# Modify the program that prompts the user for the file name
# so that it prints a funny message when the user types in the exact file
# name “na na boo boo”.
# The program should behave normally for all other files
# which exist and don’t exist.

prompt = 'Enter the file name: '
fname = input(prompt)
count = 0
try:
    if fname == 'na na boo boo':
        print('na na boo boo to you - you have been punk')
    else:
        fhand = open(fname)
except:
    print('File doesnt exist')
    quit()

if fname == 'na na boo boo':
    quit()

for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1
print('There were', count, 'subject lines in', fname)