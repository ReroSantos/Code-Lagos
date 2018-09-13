from easygui import *
import random

while True:
    msgbox("Welcome to the Number Guessing Game \nby \nOlaoluwa Adenuga \n\n\nRules:\n1) You would have to guess a number between 1-49,\n2) If your guess is lower, you would be notified and if higher you would too.\n3) You have only 5 attempts to get it right.")

    guess = random.randint(1,49)

    guess1 = integerbox(msg="Input your guess:", title="Guess #1")

    if (guess1== guess):
        msgbox(msg="Wow you got it on the first try", title="Response")

    elif (guess1<guess):
        msgbox(msg="That too low", title="Response")

    else:
        msgbox(msg="That too high", title="Response")
        
        
    guess2 = integerbox(msg="Input your guess:", title="Guess #2")

    if (guess2== guess):
        msgbox(msg="Way to go!, you nailed it on the second attempt", title="Response")

    elif (guess2<guess):
        msgbox(msg="That too low", title="Response")

    else:
        msgbox(msg="That too high", title="Response")
        
        
    guess3 = integerbox(msg="Input your guess:", title="Guess #3")

    if (guess3== guess):
        msgbox(msg="Wow, you got third time lucky", title="Response")

    elif (guess3<guess):
        msgbox(msg="That's too low", title="Response")

    else:
        msgbox(msg="That's too high", title="Response")

    guess4 = integerbox(msg="Input your guess:", title="Guess #4")

    if (guess4== guess):
        msgbox(msg="Lucky you, you got it on the penultimate attempt", title="Response")

    elif (guess4<guess):
        msgbox(msg="That's low", title="Response")

    else:
        msgbox(msg="That's high", title="Response")


    guess5 = integerbox(msg="Input your guess:", title="Final Guess")

    if (guess5== guess):
        msgbox(msg="Congrats, you got it on the Last try", title="Response")

    else:
        msgbox(msg="Sorry you lose", title="Response")
        

    msg = "Do you want to continue playing?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:  # user chose Cancel
        sys.exit(0)

