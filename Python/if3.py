print"program for calculus of circle...."


r=int(raw_input("Enter radious :"))

print"1.Area of circle:"
print"2.curcumferance:"

ch=input("Enter choice")
if ch==1:
   
    import math
    ar=math.pi*r**2
    print"Area of circle :",ar

elif ch==2:
    import math
    cu=2*math.pi*r
    print"Circumfarnce",cu

else:
    print"Enter valid choice"

raw_input("ok")
