from random import randint
from art3 import logo

easy_level_turns=10
hard_level_turns=5
turns=0


def check_answer(guess,answer,turns):
    if guess>answer:
        print("Too high.")
        return turns -1
    elif guess<answer:
        print("Too low.")
        return turns -1
    else:
        print(f"You got it! The answer is {answer}.")


def difficulty_level():
    level=input("Choose a difficulty. Type 'easy' or 'hard':")
    if level=="easy":
        return easy_level_turns
    else:
        return hard_level_turns

print(logo)
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer=randint(1,100)
    print(f"Pssst, the correct answer is {answer}")


    turns=difficulty_level()
    

    guess=0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number.")
        guess=int(input("Make a guess:"))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("You've ran out of guess, You lost.")
            return
        elif guess!=answer:
            print("Guess again")

game()
