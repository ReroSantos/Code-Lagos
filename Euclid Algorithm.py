'''x = int(input( "input the first digit: "))
y = int(input( "input the second digit: "))'''

'''if x>y:
  smaller = y
  larger = x
else:
    smaller = x
    larger = y'''

def gcd(smaller,larger):
  r = larger%smaller
  if r==0:
    return  print (smaller)
  else:
    larger = smaller
    smaller = r
    return gcd(smaller,larger)

  print ("The greatsest common divisor of ", smaller ," and ", larger ,"equals", smaller)
