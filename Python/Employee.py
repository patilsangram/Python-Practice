class Employee:
	empcount = 0
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
		Employee.empcount+=1
	def disp(self):
		print "Name :",self.name,"Salary :",self.salary
	def empcnt(self):
		print"Total employee ",Employee.empcount

emp1 = Employee('sangram',15000)
emp2 = Employee('Sourav',23000)

	

emp1.disp()
emp2.disp()
emp2.empcnt()
		
