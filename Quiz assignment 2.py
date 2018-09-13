while True:
  name = str(input("What is your name?: "))
  score = 0
  """while score == 0:"""

  answer1 = str(input("\n(1) What is the name of the first president of Nigeria? \n(a) Amadu Bello \n(b) Shehu Shagari \n(c) Olusegun Obasanjo \n(d) Nnamdi Azikwe\n:Your answer: "))

  if( answer1 == "d" ):
    score = int(score)+5
    print ( "Weldone", name, "you've scored", score, "points")
  elif( answer1.lower != "d" ):
    score = score - 5
    print( "ouch!!!", name, "you missed that, you've scored, ", score, "points")
    
  answer2 = str(input("\n(2) What is the name of the capital of Lagos state? \n(a) Ikorodu\n(b) Ikeja\n(c) Surulere\n(d) Victoria Island\nYour answer: "))

  if (answer2 == "b") :
    score = score+5
    print ( "Weldone", name, "you've scored", score, "points")
  else:
    score = score - 5
    print( "ouch!!!", name, "you missed that, you've scored, ", score, "points")

  answer3 = str(input("\n(3) What is the name of the first capital of Nigeria?\n(a) Kano \n(b) Abuja\n(c) Lagos\n(d) Calabar\nYour Answer: "))

  if (answer3 == "c"):
    score = score+5
    print ( "Weldone", name, "you've scored", score, "points")
  else:
    score = score - 5
    print( "ouch!!!", name, "you missed that, you've scored, ", score, "points")

  answer4 = str(input("\n(4) What is the name of the governor of Lagos when Code-Lagos was first implemented? \n(a)Raji Fashola\n(b)Akinwunmi Ambode\n(c) Ahmed Tinubu\n (d) Lateef Jakande\nYour answer: "))

  if (answer4 == "b"):
    score = score+5
    print ( "Weldone", name, "you've scored", score, "points")
  else:
    score = score - 5
    print( "ouch!!!", name, "you missed that, you've scored, ", score, "points")


  answer5 = str(input("\n(5) Which of the following is indigenous Nigerian content? \n(a) Etisalat\n(b) Airtel\n(c) MTN\n(d) Globacoms\n Your Answer: "))

  if (answer5 == "d") :
    score = score+5
    print ( "Weldone", name, "you've scored", score, "points")
  else:
    score = score - 5
    print( "ouch!!!", name, "you missed that, you've scored, ", score, "points")

  print("\n......................................................GAME OVER.............................................................................................................................................................................................................................................\n")

  out = str(input("Type 'play' to continue this game or 'exit' to quit playing\n: "))

  if (out=="exit"):
    break
