from sys import argv

script, filename = argv

print "file is: %s"%filename
txt = open(filename)
print txt.read()
clear_file = open(filename, 'w')
clear_file.truncate()

write_file = open(filename, 'rw+')

write_file.write("hello")
write_file.read()