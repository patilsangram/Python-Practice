c=[1,2,8,9,1,3,6,8]

     i=0
     count=0
 
while(i<len(c)):
       if c[i]==c[i+1]:
        count=count+1
        i+=1
    else:
        i+=1

    print(c[i],count)
            
