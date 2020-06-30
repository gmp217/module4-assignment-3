l,nl=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'],[]
print('original list:',l)
for i in range(0,len(l)):
	if i not in (0,4,5):
		nl.append(l[i])
print('new list:',nl)