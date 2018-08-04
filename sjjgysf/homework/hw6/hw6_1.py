# 快速指数
def calCube(a,nn):
	n = abs(nn)
	if n == 0:
		return 1
	if n == 1:
		return a
	if n % 2 == 1:
		ans = calCube(a,(n - 1) // 2)
		if nn > 0:
			return a*ans*ans
		else:
			return 1/a/ans/ans
	else:
		ans = calCube(a,n // 2)
		if nn > 0:
			return ans*ans
		else:
			return 1/ans/ans
print(calCube(2,-5))