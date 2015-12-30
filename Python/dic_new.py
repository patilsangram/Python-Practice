l1=[1,1,8,9]
l2=[1,3,6,8]
l1.extend(l2)

l3={}

for c in l1:
    print c
    l3[c]=1
    
    if l3.get(c) in l3:
        l3[c]+=1
    else:
        pass
    
print'\n'
print l3
