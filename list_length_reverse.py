#finding length of list and reversing a user-input list of prime numbers
#length
l=[1,2,3,4,5,6]
length=len(l)
print("Length of list= ",length)
#reverse
n=int(input("Enter number of elements: "))
l=[]
for i in range(n):
  e=int(input("Enter prime number: "))
  l.append(e)
print("Created list= ",l)
l.reverse()
print("Reversed list= ",l)


