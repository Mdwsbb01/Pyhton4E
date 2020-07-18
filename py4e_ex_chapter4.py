#Exercise 6: Rewrite your pay computation
# with time-and-a-half for overtime and create a function called computepay
# which takes two parameters (hours and rate).
'''
prompt1 = 'Enter the hours: '
prompt2 = 'Enter the rate: '
hrs = float(input(prompt1))
rat = float(input(prompt2))
def computepay(hrs, rat):
    if hrs > 40:
        basic = 40.0 * rat
        extra_rat = rat * 1.5
        bonus = (hrs-40.0) * extra_rat
        pay = basic + bonus
    else:
        pay = hrs * rat
    return pay
print('Pay', computepay(hrs, rat))
'''
#Exercise 7: Rewrite the grade program from the previous chapter
# using a function called computegrade that takes a score
# as its parameter and returns a grade as a string.

prompt = 'Enter the score'
scores = input(prompt)
try:
    scrs = float(scores)
except:
    print('Bad scores')

def computegrade(scrs):
    if scrs > 1.0 or scrs < 0:
        return 'Bad score'
    elif scrs >= 0.9:
        return 'A'
    elif scrs >= 0.8:
        return 'B'
    elif scrs >= 0.7:
        return 'C'
    elif scrs >= 0.6:
        return 'D'
    else:
        return 'F'

print(computegrade(scrs))