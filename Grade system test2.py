while True:''' This is to make the program to run continously
until it is terminated, hence this creates an endless loop
that has to be manually terminated.'''
    name = str(input("please enter your name: "))
    score = int(input("Please enter your score: "))


    if score > 69 and score <101:
        print ( "You got an 'A', keep it up")

    elif score > 59 and score < 70:
        print ( "You got a 'B', keep it up")

    elif score > 49  and score < 60:
        print ( "You got a 'C', you can be better")

    elif score >44 and score < 50:
        print ( "You got a 'D', Try to improve your rating")

    elif score > 39 and score <45:
        print ( "You got and 'E', your rating is poor, you definitely have to work on it ")

    elif score > 100:
        print ( "The score you inputted is invalid, scorePlease input the right score")

    else:
        print ( "you failed, go work n yourself and try again another time")
