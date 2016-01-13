class animal(object):


	def __init__(self,name,species):
		self.name = name
		self.species = species

	def getName(self):
		return self.name

	def getSpecies(self):
		return self.species

	def display(self):
		return "%s is a %s"%(self.name,self.species)

	# obj = animal()
	# obj.getName()
	# obj.getSpecies()
	# obj.display()

	# from animal import animal
	# ani = animal("motya","dog")
	print "info is %s" % getName("motya")