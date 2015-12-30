from sys import argv

script, filename = argv

print "file is: '%s'"%filename
txt = open(filename)
print'"current file"'
print txt.read()

print "'now we clear the file'"
txt = open(filename, 'w')
txt.truncate()

print "'add lines to file'"
line1 = raw_input("Line1 :")
line2 = raw_input("Line2 :")
line3 = raw_input("Line3 :")

"""you can write multiple lines once"""
txt.writelines([line1, "\n", line2, "\n", line3, "\n"])
"""OR like this one : 
txt.write("%s \n %s \n %s \n" % (line1, line2, line3))"""

"""Or you can write single lines"""
txt.write("\n")
txt.write(line2)
txt.write("\n")
txt.write(line3)
txt.write("\n")

print '"read final file"'
txt = open(filename, 'r')
print txt.read()
txt.close()

