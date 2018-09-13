while True:

  print ("Hey, Welcome to Adex BMI calculator\n")

  name= str(input("Please enter your name: "))
  h =float(input("Please input your height in meters: "))
  w = float(input("please input your weight in kilogram: "))

  bmi= int(w/h**2)
  '''
  print ("Your BMI is:", bmi)
  '''
  if (bmi <= 18.5 ):
    print("Your BMI is:", bmi, "\n You are chronically underweight, Please grab some burger\n\n...........................................................................................\n")
    
  elif (bmi > 18.5  and bmi<=24.9  ):
    print("\n..............................................................................................\nYour BMI is:", bmi, "\n You are just fine, but you can grab a bowl of chicken soup\n\n...........................................................................................\n")
    
  elif (bmi > 24.9 and bmi<= 29.9  ):
    print("Your BMI is:", bmi, "\n\nYou are overweight, watch what you eat, we've got some salad just for you\n\n...........................................................................................\n")

  else:
    print("Your BMI is:", bmi, "\n You are Obese, we can help you with our specially formulated diets\n\n...........................................................................................\n")



    
