def findGCD(a,b):
	#print(a,b)
	if a == b:
		return a
	if a < b:
		temp = a
		a = b
		b = temp
	if b == 1:
		return 1
	if a % b == 0:
		return b
	else:
		return findGCD(a-b,b)
a = 36
b = 48
L = findGCD(a,b)
g = a*b//L
print(g,L)