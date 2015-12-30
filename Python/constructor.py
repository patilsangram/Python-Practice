class construtor:
	def __init__(self,name,year,employee):
		self.name = name
		self.year = year
		self.employee = employee
	def disp(self,new_emp):
		print "Name  :",self.name
		print "Year  :",self.year
		self.employee+=new_emp
		print "Employee  :",self.employee
		


c = construtor('Indictrans',2009,25)
c.disp(5)