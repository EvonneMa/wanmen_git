# 找到间隔最大的两个素数之间的所有数
def get_primes(n):
	ans = []
	res = [True]*n
	for i in range(2,n+1):
		if res[i-1]:
			ans.append(i)
			j  = 2
			while(j*i <= n):
				res[i*j-1] = False
				j+=1
	return ans
n = 100
prime = get_primes(n)
print(prime)
start = 0
end = 1
length = end-start-1
for i in range(len(prime)-1):
	length1 = prime[i+1] - prime[i] - 1
	if length1 > length:
		start = i
		end = i+1
		length = length1
res = []
for i in range(prime[start]+1,prime[end]):
	res.append(i)
print(res)