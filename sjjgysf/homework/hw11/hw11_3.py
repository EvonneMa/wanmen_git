# 丑数
# 1.判断一个数是否是丑数
# 2.找到第k个丑数,每次取出最小的数(需要堆),分别乘以2、3、5再放进去;遇到重复则跳过
def uglyNum1(n):
	for p in [2,3,5]:
		while n%p == 0:
			n = n//p
			#print(n)
	return n == 1
import heapq
def uglyNum2(k):
	if k == 1:
		return 1
	a = [1]
	heapq.heapify(a)
	b = [2,3,5]
	last = -1
	while(k > 0):
		c = heapq.heappop(a)
		if last == c:
			continue
		last = c
		for ele in b:
			heapq.heappush(a,c*ele)
		k -= 1
	return c
#print(uglyNum1(100))
print(uglyNum2(1500))