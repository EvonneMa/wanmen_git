# print 9*9
for i in range(9):
	for j in range(i+1):
		print("%d*%d=%d  "%(j+1,i+1,(i+1)*(j+1)),end = '')
	print('\n')
