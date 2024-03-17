#finding mean and max from a user input list of 5 numbers
l=[]
for i in range(5):
  e=eval(input("Enter a number: "))
  l.append(e)
m=max(l)
print("maximum= ",m)
avg=sum(l)/5
print("Mean= ",avg)