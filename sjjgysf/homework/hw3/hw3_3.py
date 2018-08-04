# 改进递归(仅仅用递归完全比不了循环)
# 在动态规划部分还会讲到
def fibonacci(m):
	'''
	时间复杂度为2^n,因为有两个分支,每个分支又分为两个分支,形成一棵二叉树,叶结点个数为2^n
	'''
	if m == 1:
		return 1
	if m == 2:
		return 1
	return fibonacci(m-1) + fibonacci(m-2)

def fibonacci1(m):
	'''
	这个就好一点了
	'''
	if m == 1:
		return (1,0)
	a,b = fibonacci1(m-1)
	return (a+b,a)
def fibonacci2(m):
	'''
	1和2的效果就很接近了
	'''
	a = 1
	b = 1
	for i in range(2,m):
		a,b = a+b,a
	return a
m = 100
print(fibonacci2(m))
