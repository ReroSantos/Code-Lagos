import math

while True:

        print("This is console module")

        shape=int(input("What shape are you looking to solve?\n1) Circle\n2) Rectangle\n3) Square\n4) Triangle \n5) Cylinder\n6) Cone\n: "))
        print("\n...........................................................................\n")
	
        if (shape==1):
                calc=int(input("1) Area \n2) Perimeter\n: "))
                print("\n...........................................................................\n")
		
                if (calc==1):
                        r= int(input("input the radius: "))
                        solution = r**2*math.pi
		
                elif (calc==2):
                        r= int(input("input the radius: "))
                        solution = math.pi*2*r
                else:
                        solution =("invalid calculation")
	
        elif (shape==2):
                calc=int(input("1) Area \n2) Perimeter\n: "))
                print("\n...........................................................................\n")
		
                if (calc==1):
                        l= int(input("input the length: "))
                        b= int(input("input the breadth:"))
                        solution = l*b
			
                elif (calc==2):
                        l= int(input("input the length: "))
                        b= int(input("input the breadth:"))
                        solution = 2*(l+b)
	
                else:
                        solution =("invalid calculation")
	
        elif (shape==3):
                calc=int(input("1) Area \n2) Perimeter\n: "))
                print("\n...........................................................................\n")
		
                if (calc==1):
                        l= int(input("input the length: "))
                        solution = l**2
			
                elif (calc==2):
                        l= int(input("input the length: "))
                        solution = 4*l
	
                else:
                        solution =("invalid calculation")
	
        elif (shape==4):
                calc=int(input("1) Area \n2) Perimeter\n: "))
                print("\n...........................................................................\n")
		
                if (calc==1):
                        b= int(input("input the base: "))
                        h= int(input("input the height:"))
                        solution = (h*b)/2
			
                elif (calc==2):
                        l1= int(input("input the first side: "))
                        l2= int(input("input the second side:"))
                        l3= int(input("input the third side: "))
                        solution = l1+l2+l3
	
                else:
                        solution =("invalid calculation")
	
        elif (shape==5):
                calc=int(input("1) volume \n2) Surface Area\n: "))
                print("\n...........................................................................\n")
		
                if (calc==1):
                        r= int(input("input the radius: "))
                        h= int(input("input the height: "))
                        solution= math.pi*r**2

                elif (calc==2):
                        r= int(input("input the radius: "))
                        h= int(input("input the height: "))
                        solution= math.pi*r*2*h
	
                else:
                        solution = ("invalid calculation")
		
        elif (shape==6):
                calc=int(input("1) volume \n2) Surface Area\n: "))
                print("\n...........................................................................\n")
		
                if (calc==1):
                        r= int(input("input the radius: "))
                        h= int(input("input the height: "))
                        solution= (math.pi*r**2)*h/3

                elif (calc==2):
                        r= int(input("input the radius: "))
                        h= int(input("input the height: "))
                        solution= (math.pi*r*2*h)/2
	
                else:
                        solution =("invalid calculation")
	
        else:
                solution ="We've not yet cover that"

        print (solution)
	
