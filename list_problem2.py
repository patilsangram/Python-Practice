
"""Nested list element taken in flat list"""
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

"""create sublist of consecutive element"""
pack=['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
final_list=[]
sublist=[]
for i,item in enumerate(pack):
	if(i<len(pack)-1 and pack[i]==pack[i+1]):
		sublist.append(item)
	else:
		sublist.append(item)
		final_list.append(sublist)
		sublist=[]
print final_list

"""output : [[4, 'a'], [1, 'b'], [2, 'c'], [2, 'a'], [1, 'd'], [4, 'e']]"""
pack=['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
merged_list=[]
sub_list=[]
for i,item in enumerate(pack):
	if(i<len(pack)-1 and pack[i]==pack[i+1]):
		sub_list.append(item)
	else:
		sub_list.append(item)
		list_new = [len(sub_list), sub_list[0]]
		merged_list.append(list_new)
		sub_list=[]
print merged_list
