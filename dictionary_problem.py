list1 = [1,2,3,8,7,7]
list2 = [1,2,8,8,8,8,8,8,8,9]
print "list1 =",list1,"list2 =",list2
list1.extend(list2)
result_dict = {key:list1.count(key) for key in list1}
print "dict =",result_dict

