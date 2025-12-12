s=0
print("The following operations can be performed by the Calculator:-")
print("1.Addition.") 
print("2.Subtraction")
print("3.Multiplication") 
print("4.Division")
a=int(input("Enter the operation number:"))
if (a==1):
    b=int(input("enter the number of inputs"))
    for i in range(b):
        c=int(input())
        s=s+c
    print("The Summation is:",s)

if (a==2):
    b=int(input("enter the number of inputs"))-1
    d= int(input())
    for i in range(b):
       
        c=int(input())
        s=s-c
    print("The Subtraction is:",s+d)   

if (a==3):
    b=int(input("Enter the number of Inputs:"))-2
    d= int(input())
    e= int(input())
    s=d*e
    for i in range(b):
        
        c=int(input())
        s=s*c
    print("The Multiplication is:",s)

if (a==4):
    b= int(input("Enter the number of Inputs:"))-2
    d= int(input())
    e= int(input())
    s=d/e
    for i in range(b):
        
        c=int(input())
        s=s/c
    print("The Division is:",s)
