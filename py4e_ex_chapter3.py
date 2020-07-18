#https://books.trinket.io/pfe/03-conditional.html#exercises
# Exercise 1: Rewrite your pay computation to give
# the employee 1.5 times the hourly rate for hours worked above 40 hours.
'''
prompt1 = 'Enter the hours: '
prompt2 = 'Enter the rate: '
hours = input(prompt1)
rate = input(prompt2)
if float(hours) > 40:
    basic = 40.0 * float(rate)
    rate = float(rate) * 1.5
    bonus = float(float(hours)-40.0) * float(rate)
    pay = basic + bonus
    print('Pay:', pay)
else:
    pay = float(hours) * float(rate)
    print ('Pay:', pay)
'''
'''Have a question that if the hrs is not a numeric input, how can I quit immediately
# Exercise 2: Rewrite your pay program using try and except
# so that your program handles non-numeric input gracefully
# by printing a message and exiting the program.
prompt1 = 'Enter the hours: '
prompt2 = 'Enter the rate: '
hours = input(prompt1)
rate = input(prompt2)
try:
    hrs = float(hours)
    rat = float(rate)
except:
    print('Error, please enter numeric input')
    quit()

    pay = hrs * rat
    print(pay)
'''
#Exercise 3: Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error message.
prompt1 = 'Enter the score: '
scores = input(prompt1)
try:
    fscores = float(scores)
except:
    print('Bad score')
    quit()
if fscores > 1.0 or fscores < 0:
    print('Bad score')
elif fscores >= 0.9:
    print('A')
elif fscores >= 0.8:
    print('B')
elif fscores >= 0.7:
    print('C')
elif fscores >= 0.6:
    print('D')
elif fscores < 0.6:
    print('F')
else:
    print('Bad score')