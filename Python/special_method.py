# class Special_method:
# 	def __getattribute__(self,key):
# 		if key == 'color':
# 			print 'SkyBlue'
# 		else:
# 			raise 	AttributeError

# ob = Special_method()
# ob.__getattribute__('color')
 
# class Simple_class:
# 	name = "Sangram"
# 	birth_year = 1992 

# 	def simple_method(self):
# 		print "\nMethod is working..\n"

# 	def disply(self):
# 		print"Name :",self.name,"\n"
# 		print"Birth_year",self.birth_year,"\n"
# Simple_object = Simple_class()

# Simple_object.simple_method()
# Simple_object.disply()
class simple:
	name = "Sangram in swim"
	def __getattribute__(self,color):
		raise AttributeError
		
	def swim(self):
		print"No AttributeError"
		
# ob = simple()
# ob.swim()
# print ob.name