#Exercise 4: Download a copy of the file www.py4e.com/code3/romeo.txt.
# Write a program to open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split function.
# For each word, check to see if the word is already in a list.
# If the word is not in the list, add it to the list.
# When the program completes, sort and
# print the resulting words in alphabetica
'''
prompt = 'Enter the file name: '
fname = input(prompt)
fhand = open(fname)
wordlist = []
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for w in words:
        if w in wordlist:
            continue
        else:
            wordlist.append(w)
wordlist.sort()# why cannot print(wordlist.sort())
print(wordlist)
'''
#Exercise 5: Write a program to read through the mail box data
# and when you find line that starts with “From”,
# you will split the line into words using the split function.
# We are interested in who sent the message,
# which is the second word on the From line.
'''
prompt = 'Enter the file name: '
fname = input(prompt)
count = 0
try:
    fhand = open(fname)
except:
    print('Invalid file name: ', fname)
    quit()
for line in fhand:
    if line.startswith('From'):
        line = line.rstrip().split()
        count = count + 1
        print(line[1])
print('There were', count, 'lines in the file with From as the first word')
'''
#Exercise 6: Rewrite the program that prompts the user for a list of numbers
# and prints out the maximum and minimum of the numbers at the end
# when the user enters “done”.
# Write the program to store the numbers the user enters in a list
# and use the max() and min() functions to compute the maximum
# and minimum numbers after the loop completes.

prompt = 'Enter the number: '
num_max = 0
num_min = 0
num_list = []
while True:
    inp = input(prompt)
    if inp == 'done':
        break
    num = float(inp)
    num_list.append(num)
    num_max = max(num_list)
    num_min = min(num_list)
print('Maximum: ', num_max)
print('Minimum: ', num_min)

