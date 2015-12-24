"""Problem 1.01 : print last element"""

def my_list(list_1):
	if list_1:
		x = list_1[-1]
		y  = list_1[-2]
		print "last element of list :",x
		print "second last element of list :", y

"""find k th element """
		
		element_position = input("Enter position of element")
		if len(list_1) > element_position:
			print "Element at",element_position,"is :", list_1[element_position]
		else:
			print"Element not present"
		print "No of element in list :",len(list_1)
my_list([2,9,7,8])

"""reverse list"""

simple_list = [1,2,3,4,5,6,7]
list_2 = []
x = len(simple_list)-1
for ele in simple_list:
	list_2.append(simple_list[x])
	x = x-1
print list_2

"""find out whether list is palindrome"""
pali_list = [1,2,2,1]
check_list = []
for i in reversed(pali_list):
	check_list.append(i)
print pali_list 
print check_list
if pali_list == check_list:
	print "list is palindrome"
else:
	print "list not palindrome"

"""Nested list element taken in flat list"""

nest_list = ['a', ['b', ['c', 'd'], 'e']]
x = 0
flat_list = []
for i in nest_list:
	if type(i)== list:
		for x in i:
			if type(x) == list:
				for e in x: 
					print e
					flat_list.append(e)
			else:
				print x
				flat_list.append(x)
	else:
		print i
		flat_list.append(i)
print flat_list
""" Eliminate consecutive duplicates of list elements."""
a = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
b = []
for i in a:
	if i not in b:
		b.append(i)
print b