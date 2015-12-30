try:
	x = 5
	y = 0
	x/y
finally:
	print'Done : ',x/y 	
except IOError:
	print'can\'t divide by zero'



