list_one = [1,2,3,4,5,6,7,8,9]
list_two = [2,11,2,33,4,55]
list_one+=list_two
print list_one
# dict_one = {}.fromkeys(list_one,0)
# print dict_one
count = []
for i in list_one:
	count.append(list_one.count(i))
#print count
dict_one = {}
# dict_one = dict(zip(list_one,count))
if key not in dict_one.keys():
	dict_one = {list_one[n]: count[n] for n in range(len(list_one))}
print dict_one
