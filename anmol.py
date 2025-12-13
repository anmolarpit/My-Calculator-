import math
s=0
print("The following operations can be performed by the Calculator:-")
print("1.Addition.") 
print("2.Subtraction")
print("3.Multiplication") 
print("4.Division")
print("5.Square Root")
print("6.Logarithm")
print("7.Power")
print("8.Factorial")
print("9.Trig Functions")
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
    print("The Division is:",round(s,4))

if (a==5):
    b=int (input("Enter the number:"))
    s= math.sqrt(b)

    print("The square root is:",round(s,4))

if (a==6):
    b=int (input("Enter the number:"))
    c = int (input("Enter the Base number:"))
    s= math.log(b,c)

    print("The log of the number is:",round(s,4))

if (a==7):
    b= int(input("Enter the number:"))
    c= int(input("Enter the power number:"))
    s= pow(b,c)

    print("The result is:",s)

if (a==8):
    b= int(input("Enter the number"))
    s=(b)*(b-1)
    c=b-2
    for i in range(1,b):
        s=s*i
    print("The factorial is:",s/(b-1))


if (a==9):
    print("Enter [1,2,3] for [sin,cos,tan] respectively")
    print("Enter [4,5,6] for [arcsin,arccos,arctan] respectively")
    b= int (input())
    if (b==1):
        c=int(input("Enter a value [0,360]"))
        d=math.radians(c)
        s= float(math.sin(d))

        print(round(s,4))
    if (b==2):
        c=int(input("Enter a value [0,360]"))
        d=math.radians(c)
        s= float(math.cos(d))

        print(round(s,4))
    if (b==3):
        c=int(input("Enter a value [0,360]"))
        d=math.radians(c)
        s= float(math.tan(d))

        print(round(s,4))

    if (b==4):
        c=float(input("Enter a value [-1,1]:"))
        s= float(math.degrees(math.atan(c)))

        print(round(s,4))
    if (b==5):
        c=float(input("Enter a value [-1,1]:"))
        s= float(math.degrees(math.acos(c)))

        print(round(s,4))
    if (b==6):
        c=float(input("Enter a value [-1,1]:"))
        s= float(math.degrees(math.asin(c)))

        print(round(s,4))
    

else: print("Enter a valid number")