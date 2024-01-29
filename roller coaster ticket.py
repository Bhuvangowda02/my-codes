print('welcome to the roller coaster')
height=float(input('enter your height in cm?'))
age=int(input('enter your age?'))
bill=0
if height>120:
    print('you can ride')
    if age<12:
        bill= 5 
        print('ticket price is $5')
    elif age<=18:
        bill= 7
        print('ticket price is $7')
    else:
        bill= 12
        print('ticket price is $12')
    photo=input('Do you want photo?Y/N')
    if photo=='Y':
        bill+=3
        print(f'your final bill is {bill}') 
    else:
        bill+=0
        print(f'your bill is {bill}')
        
        
        
else:
    print("you can't ride")
          