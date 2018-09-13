words= ("stag", "tags", "gas", "tag", "as", "at", "gast")
score=0
word= str(input("please form a word with the following letters (G, T, S, A): "))

if (word in words):
    print ("Bravo, you got it right.")
    score=score+1
else:
    print ("Thats wrong, you can try again")

words2= ("send", "den", "end" )

word2= str(input("please form a word with the following letters (D, E, S, N): "))

if (word2 in words2):
    print ("Bravo, you got it right.")
    score=score+1
else:
    print ("Thats wrong, you can try again")


print ("You scored",score, "/2")
