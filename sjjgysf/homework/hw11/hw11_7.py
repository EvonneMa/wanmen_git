# IPO
from heapq import *
def IPO(profits,capital,k,w):
	a = []
	for i in range(len(profits)):
		a.append((profits[i],capital[i]))
	a.sort(key = lambda x:x[1])
	item = 0
	poss = []
	j = 0
	while(item < k):
		while(j < len(a) and a[j][1] <= w):
			heappush(poss,-a[j][0])
			j += 1
		w -= heappop(poss)
		item += 1
	print(w)
k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]
IPO(profits,capital,k,w)