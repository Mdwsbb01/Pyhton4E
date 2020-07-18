'''
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
'''
'''
#Exercise 1: Write a program which repeatedly reads numbers until
# the user enters "done". Once "done" is entered,
# print out the total, count, and average of the numbers.
# If the user enters anything other than a number,
# detect their mistake using try and except
# and print an error message and skip to the next number.
count = 0
total = 0.0

while True:
    prompt = 'Enter a number: '
    thing = input(prompt)
    if thing == 'done':
        break
    try:
        num = float(thing)
    except:
        print('Invalid input')
        continue
    num = float(thing)
    print(num)
    count = count + 1
    total = total + num
    avg = total / count

print(total, count, avg)

#思路：先构建一个计算sum count avg的循环，接着插入在前面插入done的判定条件，最后处理invalid data
'''

# Exercise 2: Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum
# and minimum of the numbers instead of the average.

prompt = 'Enter the number: '
initial_value = 0.0
while True:
    thing = input(prompt)
    if thing == 'done':
        break
    try:
        num = float(thing)
    except:
        print('Invalid input')
        continue
    num = float(thing)
    if num > initial_value:
        max = num
        min = initial_value
    else:
        min = num
print('Max', max)
print('Min', min)

#问题关键在于怎么把最大最小值保存住