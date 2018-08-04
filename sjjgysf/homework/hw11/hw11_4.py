# 寻找和最小的前k个组合
# a、b两个数组,各取一个表示组合
import heapq
class node:
	def __init__(self,u,v):
		self._sum = u + v
		self._item = (u,v)
	def __lt__(self,other):
		return self._sum < other._sum
	def __eq__(self,other):
		return self._sum == other._sum
	def getItem(self):
		return self._item
def findKPairs1(a,b,k):
	c = []
	def push(i,j):
		if i < len(a) and j < len(b):
			heapq.heappush(c,[a[i]+b[j],i,j])
	push(0,0)
	pairs = []
	while(c and len(pairs) < k):
		_,i,j = heapq.heappop(c)
		pairs.append([a[i],b[j]])
		push(i,j+1)
		if j == 0:
			push(i+1,0)
	return pairs
def findKPairs(a,b,k):
	res = []
	temp = []
	for i in range(min(k,len(b))):
		heapq.heappush(temp,node(a[0],b[i]))
	for ele in a[1:k]:
		largest = heapq.nlargest(1,temp)
		for i in range(k):
			c = node(ele,b[i])
			res.append(heapq.heappushpop(temp,c).getItem())
			if c == largest[0]:
				break
	if len(res) < k:
		for i in range(k - len(res)):
			res.append(heapq.heappop(temp).getItem())
	return res[:k]
#a = [1,7,11]
#b = [2,4,6]
#k = 3
a = [1,1,3]
b = [1,2,3]
k = 3
print(findKPairs(a,b,k))
print(findKPairs1(a,b,k))