country_counter = {}
def addone(country):
	if country in country_counter:
		country_counter[country] += 1
	else:
		country_counter[country] = 1
addone('china')
addone('japan')
addone('china')
print len(country_counter)