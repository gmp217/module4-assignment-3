l,n=[],int(input('Enter no of elements: '))
print('Enter elements: ')
for i in range(0,n):
	i=input()
	l.append(i)
l2,id,m=[],[],int(input('Enter no of elements: '))
print('Enter elements: ')
for i in range(0,m):
	i=input()
	l2.append(i)
difference=set(l).symmetric_difference(set(l2))
listd= list(difference)
print(listd)