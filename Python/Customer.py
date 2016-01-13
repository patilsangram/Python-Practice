class MyClass:
 	Greeting = ""
 	def __init__(self, Name):
  		self.Greeting = Name + "!"
 	def SayHello(self):
  		print("Hello {0}".format(self.Greeting))

myc = MyClass("Sangram")
myc.SayHello()


