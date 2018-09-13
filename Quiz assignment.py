name = str(input("What is your name?: "))
score = 0
"""while score == 0:"""

answer1 = str(input("(1) What is the name of the first president of Nigeria? \n(a) Amadu Bello \n(b) Shehu Shagari \n(c) Olusegun Obasanjo \n(d) Nnamdi Azikwe\n:Your answer: "))

if answer1 == "d" or "D" or "Nnamdi" or "Nnamdi Azikwe" and "Azikwe":
    score = score+5
    print ( "Weldone", name, "you've scored", score, "points")
else:
    score = score - 5
    print( "ouch!!!", name, "you missed that, you've scored, ", score, "points")
    

answer2 = str(input("(2) What is the name of the capital of Lagos state? \n(a) Ikorodu\n(b) Ikeja\n(c) Surulere\n(d) Victoria Island\nYour answer: "))

if answer2 == "a" or "A" or "Ikeja":
    score = score+5
    print ( "Weldone", name, "you've scored", score, "points")
else:
    score = score - 5
    print( "ouch!!!", name, "you missed that, you've scored, ", score, "points")


answer3 = str(input("(3) What is the name of the first capital of Nigeria?\n(a) Kano \n(b) Abuja\n(c) Lagos\n(d) Calabar\nYour Answer: "))

if answer3 == "c" or "C" or "lagos" and "Lagos":
    score = score+5
    print ( "Weldone", name, "you've scored", score, "points")
else:
    score = score - 5
    print( "ouch!!!", name, "you missed that, you've scored, ", score, "points")


answer4 = str(input("(4) What is the name of the governor of Lagos when Code-Lagos was first implemented? \n(a)Raji Fashola\n(b)Akinwunmi Ambode\n(c) Ahmed Tinubu\n (d) Lateef Jakande\nYour answer: "))

if answer4 == "b" or "B" or "Ambode" or "Akinwunmi Ambode" or "akinwunmi ambode":
    score = score+5
    print ( "Weldone", name, "you've scored", score, "points")
else:
    score = score - 5
    print( "ouch!!!", name, "you missed that, you've scored, ", score, "points")


answer5 = str(input("(5) Which of the following is indigenous Nigerian content? \n(a) Etisalat\n(b) Airtel\n(c) MTN\n(d) Globacoms\n Your Answer: "))

if answer5 == "d" or "D" or "glo" or "Glo" or "GLO":
    score = score+5
    print ( "Weldone", name, "you've scored", score, "points")
else:
    score = score - 5
    print( "ouch!!!", name, "you missed that, you've scored, ", score, "points")
