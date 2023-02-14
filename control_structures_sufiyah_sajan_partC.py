#control structures
#sufiyah sajan
#part C

import random
number = random.randint(1,11)
print("I'm thinking of a number between 1 and 11.")
guess1 = input("Guess my number: ")
if float(guess1) == float(number):
    print("You got it!")
    print("It took you 1 try to guess the number")
elif float(guess1) > float(number):
    print("Too high, try again.")
    guess2 = input("Guess my number: ")
    if float(guess2) == float(number):
        print("You got it!")
        print("It took you 2 try to guess the number")
    elif float(guess2) > float(number):
        print("Too high, try again.")
        guess3 = input("Guess my number: ")
        if float(guess3) == float(number):
            print("You got it!")
            print("It took you 3 try to guess the number")
        elif float(guess3) > float(number):
            print("Sorry, game over.")
        elif float(guess3) < float(number):
            print("Sorry, game over.")
    elif float(guess2) < float(number):
        print("Too low, try again.")
        guess3 = input("Guess my number: ")
        if float(guess3) == float(number):
            print("You got it!")
            print("It took you 3 try to guess the number")
        elif float(guess3) > float(number):
            print("Sorry, game over.")
        elif float(guess3) < float(number):
            print("Sorry, game over.")
elif float(guess1) < float(number):
    print("Too low, try again.")
    guess2 = input("Guess my number: ")
    if float(guess2) == float(number):
        print("You got it!")
        print("It took you 2 try to guess the number")
    elif float(guess2) > float(number):
        print("Too high, try again.")
        guess3 = input("Guess my number: ")
        if float(guess3) == float(number):
            print("You got it!")
            print("It took you 3 try to guess the number")
        elif float(guess3) > float(number):
            print("Sorry, game over.")
        elif float(guess3) < float(number):
            print("Sorry, game over.")
    elif float(guess2) < float(number):
        print("Too low, try again.")
        guess3 = input("Guess my number: ")
        if float(guess3) == float(number):
            print("You got it!")
            print("It took you 3 try to guess the number")
        elif float(guess3) > float(number):
            print("Sorry, game over.")
        elif float(guess3) < float(number):
            print("Sorry, game over.")

print("The secret number was ", number)
