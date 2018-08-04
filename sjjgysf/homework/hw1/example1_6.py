# ���С��N����������
# ��°ͺղ���
n = 100
def find_prime(n):
	'''
	�Կռ任ȡ����ʱ��,����һ�Ŵ��,����������ΪFalse
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
	ֻ��Ҫ����ָ�뼴��
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