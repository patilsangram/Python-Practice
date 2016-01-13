
from Parent import Parent
from Child import Child

class Inheritance(Parent,Child):
	def all_info(self):
		print"Calling from Main.."

obj = Main()
obj.all_info()
obj.info_child()
obj.info_parent()
		
