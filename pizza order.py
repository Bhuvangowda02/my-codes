print('Welcome to shake Pizza')
size=input('Enter the size of Pizza You want:s,m,l?')
pepperoni=input('do you want pepperoni?y or n')
cheese=input('Do you need extra cheese?y or n')
bill=0
if size=='s':
    bill+=20
elif size=='m':
    bill+=25
else:
    bill+=35

if pepperoni=='y':
    bill+=5
else:
    bill+=0
    
if cheese=='y':
    bill+=10
else:
    bill+=0

print(f'your bill is ${bill}')



print('Welcome to Meow Meow Pizza')
size=input('Enter the size of Pizza You want:s,m,l?')
pepperoni=input('do you want pepperoni?y or n')
cheese=input('Do you need extra cheese?y or n')
bill=0
if size=='s':
    bill+=20
if size=='m':
    bill+=25
if size=='l':
    bill+=30

if pepperoni=='y':
    bill+=9
else:
    bill+=0
if cheese=='y':
    bill+=18
else:
    bill+=0
print(f"your bill is ${bill}")