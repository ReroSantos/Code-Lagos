

t = float(input("what is the duration of the loan in months?:  ")); #This is to ask for the time of investment
p= int(input("What is the value of loan at receipt?:  ")); #This is to ask for the principal borrowed
r= float(input("what is the fixed interest rate?:  ")); #This is to ask for the interest rate

i = (p*t*r)/100; #This is to calculate for simple interest

A = p+i; #This is to calculate for the total value to be repayed.


#This begins the print section

print ("The value of the expected interest is: " + str(i));
print (" The total value of the expected pay for the loan: " + str(A));

# OR you can still try it this way without having to convert the values to strings.
"""
print ("The value of the expected interest is: ");
print(i);
print (" The total value of the expected pay for the loan: ");
print(A);

"""
# you can uncomment the above multi-line comments to test it out.
