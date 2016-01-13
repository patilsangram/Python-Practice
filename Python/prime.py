for num in range(5,10 ):
	for i in range(2,num):
		x=num%i
		z=num/i
		if x==0:
			print "%d is %d * %d "%(num,i,z)
			break
		else:
			print "% is prime no. "%num
			break
