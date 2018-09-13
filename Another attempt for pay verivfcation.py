name= str(input("Please enter your name: "))
paid= int(input("Please enter the amount paid: "))

expected = 10000

if expected == paid:
    print( "Ade, Thanks for your payment")
else:
    if expected > paid:
      print( "Dear Ade, you have a balance of ", (expected - paid), "to pay, kindly pay up")
    else:
      print(" You are due for a refund of", (paid - expected), ", kindly go through the appropriate channels")
