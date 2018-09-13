from easygui import *
import random
import math

while True:
    msgbox("Welcome to the Number Guessing Game \nby \nOlaoluwa Adenuga \n\n\nRules:\n1) You would have to guess a number between 1-99,\n2) If your guess is lower, you would be notified and if higher you would too.\n3) You have only 5 attempts to get it right.")

    guess = random.randint(1,99)

    guess1 = integerbox(msg="Input your guess:", title="Guess #1")

    if (guess1== guess):
        msgbox(msg="Wow you got it on the first try", title="Response")
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

    guess2 = integerbox(msg="Input your guess:", title="Guess #2")

    if (guess2== guess):
        msgbox(msg="Bravo, you got it on the second try", title="Response")
        break

    else:
        if (guess2>guess) and ((guess2-guess) >10):
            msgbox(msg="That's too high", title="Response")
            
        elif (guess2>guess) and ((guess2-guess) <=10):
            msgbox(msg="That's high", title="Response")

        elif (guess2<guess) and ((guess-guess2) >10):
            msgbox(msg="That's too low", title="Response")

        elif (guess2<guess) and ((guess-guess2) <10):
            msgbox(msg="That's low", title="Response")

        else:
            pass

    guess3 = integerbox(msg="Input your guess:", title="Guess #3")

    if (guess3 == guess):
        msgbox(msg="Wow, you got lucky on the third attempt", title="Response")
        break

    else:
        if (guess3 >guess) and ((guess3 - guess) >10):
            msgbox(msg="That's too high", title="Response")
            
        elif (guess3 >guess) and ((guess3 - guess) <=10):
            msgbox(msg="That's high", title="Response")

        elif (guess3 <guess) and ((guess - guess3) >10):
            msgbox(msg="That's too low", title="Response")

        elif (guess3 <guess) and ((guess - guess3) <10):
            msgbox(msg="That's low", title="Response")

        else:
            pass

    guess4 = integerbox(msg="Input your guess:", title="Guess #4")

    if (guess4 == guess):
        msgbox(msg="Wow you got it on your penultimate attempt", title="Response")
        break

    else:
        if (guess4 >guess) and ((guess4-guess) >10):
            msgbox(msg="That's too high", title="Response")
            
        elif (guess4>guess) and ((guess4-guess) <=10):
            msgbox(msg="That's high", title="Response")

        elif (guess4<guess) and ((guess-guess4) >10):
            msgbox(msg="That's too low", title="Response")

        elif (guess4<guess) and ((guess-guess4) <10):
            msgbox(msg="That's low", title="Response")

        else:
            pass

    guess5 = integerbox(msg="Input your guess:", title="Final Guess")

    if (guess5== guess):
        msgbox(msg="Congrats, you got it on the final try", title="Response")

    else:
        if (guess5>guess) and ((guess5-guess) >10):
            msgbox(msg="That's too high", title="Response")
            
        elif (guess5>guess) and ((guess5-guess) <=10):
            msgbox(msg="That's high", title="Response")

        elif (guess5<guess) and ((guess-guess5) >10):
            msgbox(msg="That's too low", title="Response")

        elif (guess5<guess) and ((guess-guess5) <10):
            msgbox(msg="That's low", title="Response")

        else:
            pass

    msg = "Do you want to play another game?"
    title = "Please Confirm"
    if ccbox(msg="GAME OVER\n would you like to play another game?", title="Game Over"):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:  # user chose Cancel
        sys.exit(0)

