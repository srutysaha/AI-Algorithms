#check if an alphabet is vowel or consonant
a=input("Enter an alphabet: ")
if(a.lower() in "aeiou"):
  print("vowel")
elif(a.lower() in "bcdfghjklmnpqrstvwxyz"):
  print("consonant")
else:
  print("not an alphabet")
