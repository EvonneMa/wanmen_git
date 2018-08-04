def pow(a,b):
	if b == 1:
		return a
	if b % 2 == 1:
		ans = pow(a,b // 2)
		return ans*ans*a
	else:
		ans = pow(a,b // 2)
		return ans*ans
print(pow(2,10))