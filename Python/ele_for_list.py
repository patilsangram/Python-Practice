list=[]
for length in range(0,int(raw_input("Enter length:"))):
		print "Enter element for list"
                list.append(raw_input("Enter :"))
list=map(int,list)
print 'sum of element :',sum(list)
print 'multiplication of element :',reduce(lambda a,b:a*b,list)
print list
raw_input("Done......")
