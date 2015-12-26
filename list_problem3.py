"""1.11  	Modified run-length encoding.
			?- encode_modified([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
			X = [[4,a],b,[2,c],[2,a],d,[4,e]]  """

pack = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']

sublist = []
list_of_sublist = []

for i,item in enumerate(pack):
	if i<len(pack)-1 and pack[i] == pack[i+1]:
		sublist.append(item)
	else:
		sublist.append(item)
		if len(sublist)>1:
			sublist = [len(sublist),sublist[0]]
			list_of_sublist.append(sublist)
			sublist = []
		else:
			list_of_sublist.append(item)
			sublist = []

print list_of_sublist


"""1.12 construct uncompressed version of list e.g. X = [[4,a],b,[2,c],[2,a],d,[4,e]] """
compressed_list = [[4,'a'],'b',[2,'c'],[2,'a'],'d',[4,'e']]

uncompressed_list = []
for i, item in enumerate(compressed_list):
	if type(compressed_list[i]) == list: 
		for ele in range(0,item[0]):
			uncompressed_list.append(item[1])
	else:
		uncompressed_list.append(item)
print uncompressed_list

"""1.14 Duplicate the elements of a list.
			Example:
			dupli([a,b,c,c,d],X).
			X = [a,a,b,b,c,c,c,c,d,d] """


simple_list = ['a','b','c','c','d']
duplicate_list = []
for i in simple_list:
	duplicate_list.append(i)
	duplicate_list.append(i)
print duplicate_list

""" 1.15 Duplicate the elements of a list a given number of times."""
def dupli_list_method(simply_list,x):
	dupliy_list = []
	for i,item in enumerate(simply_list):
		for ele in range(0,x):
			dupliy_list.append(item)
	print dupliy_list

dupli_list_method(['a','b','c','c','d'],3)

# pack = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']

# for i, item in enumerate(pack):
# 	count = 0
# 	if i<len(pack)-1 and pack[i] == pack[i+1]:
# 		count += 1
# 		pack.insert(i,count)
# 	else:
# 		count = 1
# 		pack[i] = count
# print pack

