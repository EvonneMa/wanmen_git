# 改进的Fibonacci——O(lgn)
# 利用矩阵,类似快速指数,加快计算速度
#	[[1,1],[1,0]]^n = [[f(n+1),f(n)],[f(n),f(n-1)]]
def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return [[1,1],[1,0]]
	if n % 2:
		ans = fibonacci(n//2)
		a = ans[0][0]*ans[0][0]+ans[0][1]*ans[1][0]
		b = ans[0][0]*ans[0][1]+ans[0][1]*ans[1][1]
		c = ans[1][0]*ans[0][0]+ans[1][1]*ans[1][0]
		d = ans[1][0]*ans[0][1]+ans[1][1]*ans[1][1]
		return [[a+b,a],[c+d,c]]
	else:
		ans = fibonacci(n//2)
		a = ans[0][0]*ans[0][0]+ans[0][1]*ans[1][0]
		b = ans[0][0]*ans[0][1]+ans[0][1]*ans[1][1]
		c = ans[1][0]*ans[0][0]+ans[1][1]*ans[1][0]
		d = ans[1][0]*ans[0][1]+ans[1][1]*ans[1][1]
		return [[a,b],[c,d]]
print(fibonacci(15)[0][1])