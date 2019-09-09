corridor = []
# this creates a list with the 100 rooms, False meaning the door being closed.
for i in range(100):
	corridor.append(False)

def entrynumber():
	x = 1
	while x < len(corridor):
		for e in range(0,len(corridor),x):
			if corridor[e] == False:
				corridor[e] = True
			elif corridor[e] == True:
				corridor[e] = False
		x += 1

entrynumber()

print(corridor)

open_doors = []


for e in corridor:
	if e == True:
		print(corridor.index(e))




