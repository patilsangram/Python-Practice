try:
	fh = open("Indictrans", "w")
	fh.write("This is my test file for exception handling!!\n ")
except IOError:
	print "Error: can\'t find file or read data"
else:
	print "Written content in the file successfully"
	fh.close()