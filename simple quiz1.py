score=0
name = str(input ("please input your name: "))
print ("Welcome", name)
 
answer1=str(input ("(1) How many Out of school centers does CodeLagos have?\n(A) 4\n(B)12\n(C) 21\n(D)30\n What is your answer: "))

if answer1 == "C":
     print ( "Correct!!!, Your score is", score+1, "out of 1" )
     score = score+1
else:
    print ("wrong, your score is", score, "out of  1")

answer2 = str(input ("(2) In what year did CodeLagos start?\n(A) 2017\n(B) 2012\n(C) 1999\n(D) 2018\n What is your answer: "))

if answer2 == "A":
     print ( "Correct!!!, Your score is", score+1, "out of  2")
     score = score+1
else:
    print ("wrong, your score is", score, "out of  2")

answer3 = str(input("(3) How many Lagosians does CodeLagos intends to train by year 2020?\n(A) 50,000\n(B) 2,000,000\n(C) 600,000\n(D) 1,000,000\n What is your answer: "))

if answer2 == "D":
     print ( name, "Correct!!!, Your score is", score+1, "out of 3" )
     score= score+1
else:
    print (name, "wrong, your score is", score, "out of  3")         
