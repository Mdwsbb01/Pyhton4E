# EX.2: Hello Dongxiao
prompt = 'Enter your name: \n'
name = input(prompt)
print('Hello ', name)

# EX.3: Calculate Pay
prompt1_hours = 'Enter the hours: \n'
prompt2_rate = 'Enter the rate per hour: \n'
hours = input(prompt1_hours)
rate = input(prompt2_rate)
pay = float(hours) * float(rate)
print('Pay: \n', pay)

# EX.4: Value and type
width = 17
height = 12.0
exp1 = width // 2
exp2 = width / 2.0
exp3 = height / 3
exp4 = 1 + 2 ** 5
print(exp1, type(exp1))
print(exp2, type(exp2))
print(exp3, type(exp3))
print(exp4, type(exp4))