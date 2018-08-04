# 数组中第k大的元素
# 可以用快速排序解决(比heapq快)
# 可以用堆解决,且堆的大小为k即可
import heapq
def findKthLargest(nums,k):
	return heapq.nlargest(k,nums)[-1]
import numpy as np
nums = np.random.permutation(10)
print(findKthLargest(nums,5))