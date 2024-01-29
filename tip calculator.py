print('Welcome to the tip calculator')
bill=(float(input('what is the total bill?$')))
tip=(int(input('what percentage tip would you like to give?10, 12 or 15?')))
people=(int(input('how many people to split the bill?')))
a=tip/100
b=bill*a
c=bill+b
d=round(c/people,2)
print(f'Each person should pay ${d}')
