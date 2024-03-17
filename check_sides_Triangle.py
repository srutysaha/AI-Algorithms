#check sides of a triangle
a=eval(input("Enter side 1: "))
b=eval(input("Enter side 2: "))
c=eval(input("Enter side 3: "))
if(a+b>c or a+c>b or b+c>a):
    print("Triangle possible!")
    if(a>0 and b>0 and c>0):
      if(a==b and b==c and c==a):
        print("Equilateral Triangle")
      elif(a==b or b==c or c==a):
        print("Isosceles Triangle")
      else:
        print("Scalene Triangle")
    else:
      print("Not a triangle")

else:
    print("Triangle not possible")