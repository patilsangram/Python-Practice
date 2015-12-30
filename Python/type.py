v = input("Enter anything :")
try:
	val = int(v)
	print"%d is int"%val

except ValueError:
	frappe.throw(_("Enter valid ID "))
	

