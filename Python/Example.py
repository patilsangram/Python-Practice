class Example:
	#name = "Sangram"
	#age = 23
	def info(self,a,b):
		print a+b
		#str = "Sangram"
		self.name = "Sangram"
		self.age = 23
		#print var
		print self.name,"\n", self.age

obj = Example()
obj.info(2,3)

