'''Adenuga Olaoluwa Temitope
adenugaolaoluwa@gmail.com
github:Rerosantos

oriz4freeman@gmail.com
'''

from easygui import *
import random
import math

while True:
    msgbox("Welcome to the Number Guessing Game \nby \nOlaoluwa Adenuga \n\n\nRules:\n1) You would have to guess a number between 1-99,\n2) If your guess is lower, you would be notified and if higher you would too.\n3) You have only 5 attempts to get it right.")

    guess = random.randint(1,99)

    for i in range(1,6):
        guess1 = integerbox(msg="Input your guess:", title="Guess ")

        if (guess1== guess):
            msgbox(msg="Wow you got it ", title="Response")
            break

        else:
            if (guess1>guess) and ((guess1-guess) >10):
                msgbox(msg="That's too high", title="Response")
            
            elif (guess1>guess) and ((guess1-guess) <=10):
                msgbox(msg="That's high", title="Response")

            elif (guess1<guess) and ((guess-guess1) >10):
                msgbox(msg="That's too low", title="Response")

            elif (guess1<guess) and ((guess-guess1) <10):
                msgbox(msg="That's low", title="Response")

            else:
                pass

        msg = "Do you want to continue playing?"
        title = "Please Confirm"
        if ccbox(msg, title):     # show a Continue/Cancel dialog
            pass  # user chose Continue
        else:  # user chose Cancel
            sys.exit(0)
