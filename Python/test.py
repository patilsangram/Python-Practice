l1=[1,2,8,9]
l2=[1,3,6,8]

l1.extend(l2)
print l1
dic={}

for ele in l1:
    if dic.get(ele):
        dic(ele)+=1
    else:
        dic(ele)=1
