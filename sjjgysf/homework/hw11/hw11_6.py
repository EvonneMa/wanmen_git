# 寻找中位数
# 未知长度的数据流
# 两种方法：两个链表或两个堆,两个堆还是快啊
# 一个记录较大值,一个记录较小值
from heapq import *
class MedianFinder:
	def __init__(self):
		self.heaps = [],[]
	def addNum(self,num):
		small,large = self.heaps
		heappush(small,-heappushpop(large,num))
		if len(small) > len(large) + 1:
			heappush(large,-heappop(small))
	def findMedian(self):
		small,large = self.heaps
		if len(small) == len(large):
			return (large[0] - small[0]) / 2
		else:
			return -small[0]
mf = MedianFinder()
nums = [1,4,6,8,2,3,7,9,8]
for i in nums:
	mf.addNum(i)
	print(mf.findMedian())