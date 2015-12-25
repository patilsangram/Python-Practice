
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

# """create sublist of consecutive element"""
# pack=['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
# ilist=[]
# nlist=[]
# for i,item in enumerate(pack):
# 	if(i<len(pack)-1 and pack[i]==pack[i+1]):
# 		nlist.append(item)
# 	else:
# 		nlist.append(item)
# 		ilist.append(nlist)
# 		nlist=[]
# print ilist

# """output : [[4, 'a'], [1, 'b'], [2, 'c'], [2, 'a'], [1, 'd'], [4, 'e']]"""
# pack=['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
# ilist=[]
# nlist=[]
# for i,item in enumerate(pack):
# 	if(i<len(pack)-1 and pack[i]==pack[i+1]):
# 		nlist.append(item)
# 	else:
# 		nlist.append(item)
# 		list_new = [len(nlist), nlist[0]]
# 		ilist.append(list_new)
# 		nlist=[]
# print ilist
