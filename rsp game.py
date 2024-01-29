rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
list=[rock,paper,scissors]
user=int(input('enter your choice:type 0 for rock,1 for paper,2 for scissors?'))
if user>2 or user<0:
      print('invalid number,You loose')
else:
    print(list[user])
    comp=random.randint(0,2)
    print(f'computer choose:')
    print(list[comp])


    if comp>user:
        print('youloose')
    elif comp==0 and user==2:
        print('you win!')
    elif comp==2 and user==0:
        print('you loose')
    elif comp==user:
        print('its a draw')

    else:
        print('You wins')