while True:
 #Display the options
 #Ask the user to make a choice
  x = str(input("Please select an option \n1) Create\n2)Read\n3)Save\n4)Delete\n5)Edit\n:"))
  menu=x.lower
  
 #print out user's choice
  if menu=="exit":
    break

  if (menu=="Create"):
    print("\nCreate")
    
  elif(menu=="Read"):
    print("\nRead")

  elif(menu=="Save"):
    print("\nSave")

  elif(menu=="Delete" or 4):
    print("\nDelete")

  elif menu=="Edit":
    print("\nEdit")

  else:
    print("\nInvalid option")

    print("\n................................................................................................................\n")

  
