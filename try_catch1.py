import sys

while True:
   try:
       x = int(input("Enter an integer: "))
       r = 1/x
       break
   except:
       print("Oops!",sys.exc_info()[0],"occured.")
       print("Please try again.")
       print()

print("The reciprocal of",x,"is",r)