#fibonacci series
def fibonacci(num):
    if(num>=0):
        if(num==0):
            return num
        elif(num==1):
            return num
        else:
            return fibonacci(num-1)+fibonacci(num-2)
    else:
        print("Negative number! Can't find series.")
    
#main
n=int(input("Enter a number: "))
for i in range(n):
    print(fibonacci(i),end='\t')