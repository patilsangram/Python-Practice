class Child:
	'child class'
	def __init__(self,name):
		self.name=name
	
	def msg(self):
		print"Hi ",self.name
Childobj = Child("Sangram")
Childobj.msg()
