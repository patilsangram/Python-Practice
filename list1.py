"""Print last, second last element"""

def my_list(list_1):
	if len(list_1)>1:
		x = list_1[-1]
		y  = list_1[-2]
		print "last element of list :",x
		print "second last element of list :", y
	elif len(list_1) == 1:
		x = list_1[-1]
		print "last element of list :",x
	else:
		print "check input list"
my_list([1,2,3])

"""find k th element """
def my_list(list_1,element_position):		
	# element_position = raw_input("Enter position of element")
	if len(list_1) > element_position:
		print "Element at",element_position,"is :", list_1[element_position]
	else:
		print"Element not present"
	print "No of element in list :",len(list_1)
my_list([2,9,7,8],2)

"""reverse list"""

simple_list = [1,2,3,4,5,6,7]
list_2 = []
x = len(simple_list)-1
for ele in simple_list:
	list_2.append(simple_list[x])
	x = x-1
print simple_list
print list_2

"""find out whether list is palindrome"""
pali_list = [1,2,2,5]
print pali_list 

if pali_list == pali_list[::-1]:
	print "list is palindrome"
else:
	print "list not palindrome"

""" Eliminate duplicates of list elements."""
a = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
b = []
for i in a:
	if i not in b:
		b.append(i)
print b


""" Eliminate consecutive duplicates of list elements."""
duplicates_list = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
output_list = []
output_list.append(duplicates_list[0])
i = 0
for ele in duplicates_list:
	if ele == output_list[i]:
		pass
	else: 
		i+=1
		output_list.append(ele)
print output_list

flatten_list = []

def flat_list(nested_list):
	
	for element in nested_list:
		if isinstance(element, list):
			flat_list(element)
		else:
			flatten_list.append(element)

nest_list = ['a',['b',['c','d'],'e']]
flat_list(nest_list)
print flatten_list