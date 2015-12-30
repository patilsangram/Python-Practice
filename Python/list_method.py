len=int(raw_input("Enter length :"))
list=[]

for ele in range(len):
	input=raw_input("Enter element for list :")
	list.append(input)
print list

while True:
	method=int(raw_input(" 1.Add \n 2.Remove \n 3.Reverse \n 4.Display \n 5.Delete \n 6.Exit"))

	if method==1:
		add=raw_input("Enter to add : \n")
		list.append(add)
		print"list after adding...",list,"\n"
	elif method==2:
		remove_ele=raw_input("Remove element : \n")
		list.remove(remove_ele)
		print"After remove \n",list
	elif method==3:
		list.reverse()
		print list
	elif method==4:
		print "Your List ", list
	elif method==5:
		del_ele=int(raw_input("Enter index of del ele : \n"))
		if del_ele in list:
			del list[del_ele]
			print list
		else:
			print "element not present"
	elif method ==6:
		exit()
	else:
		print"Enter valid choice :\n"
