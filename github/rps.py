import random
import keyboard
import time
res = 0 
auto = 0
while True:
    
 print("WELCOME TO ROCK|PAPER|SCISSORS")
 a= int(input("Choose \n1.Rock \n2.Paper \n3.Scissors \nEnter:"))
 if (a == 1):
    print("Your choice is Rock")
 elif (a == 2):
    print("Your choice is Paper")
 elif (a == 3):
    print("Your choice is Scissors")

 
 b= random.randint(1,3)
 time.sleep(1.5)
 if (b == 1):
    auto="Rock"
 elif (b == 2):
    auto="Paper"
 elif (b == 3):
    auto="Scissors"
 print("Now the computer choice is..", auto)
 time.sleep(1)

 if (a == 1 and b== 1):
    res="DRAW"
 elif(a==1 and b == 2):res="LOST"
 elif(a==1 and b==3):res="------WON------"

 if (a == 2 and b== 2):
    res="DRAW"
 elif(a ==2 and b == 3):res="LOST"
 elif (a==2 and b==1):res="------WON------"

 if (a == 3 and b== 3):
    res="DRAW"
 elif(a ==3 and b == 1):res="LOST"
 elif(a == 3 and b ==2):res="------WON------"

 if (res=="DRAW"):
    print("SAME CHOICE, QUITE STRANGE...")
 elif(res=="LOST"):
    print("<<COMPUTER WINS>>")
    print("YOU WILL WIN AGAIN NEXT TIME....")
 elif(res=="------WON------"):
    print("<<YOU WON>>")
    print("SO PROUD SO PROUD")
 time.sleep(2)
 print("DO YOU WANT TO PLAY AGAIN? Y/N")
 c= input()
 time.sleep(1)

   
 if (c=="N" or c=="n"):
    print("THANK YOU FOR PLAYING")
    break
 elif(c=="Y" or c=="y"):
    pass
 else:
    print("enter a valid key")
    pass
 