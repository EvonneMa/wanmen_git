# 输出小于N的所有质数
# 哥德巴赫猜想
n = 100
def find_prime(n):
	'''
	以空间换取计算时间,建立一张大表,遇到倍数置为False
	'''
	res = []
	primes = [True]*n
	for i in range(2,n+1):
		if primes[i-1]:
			res.append(i)
			j = 2
			while(j*i <= n):
				primes[j*i-1] = False
				j+=1
	return res
res = find_prime(n)
print(res)
def goldbach(n):
	'''
	只需要两个指针即可
	'''
	primes = find_prime(n)
	a = 0
	b = len(primes)-1
	while(a<=b):
		sums = primes[a] + primes[b]
		if sums > n:
			b -= 1
		elif sums < n:
			a += 1
		else:
			return (primes[a],primes[b])
	return False
res = goldbach(n)
print(res)