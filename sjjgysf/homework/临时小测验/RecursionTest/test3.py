def multi(a,b):
	if b == 0:
		return 0
	if b == 1:
		return a
	if b%2 == 1:
		return 2*(multi(a,b // 2)) + a
	else:
		return 2*(multi(a,b // 2))
print(multi(100,100))