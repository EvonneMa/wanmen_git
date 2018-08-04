# 计数排序(桶排序)(抽屉排序)
# 数字比较集中(即数字范围不是很大)、有较多重复项
# O(n)
def countSort(nums):
	mmax = nums[0]
	mmin = nums[0]
	for ele in nums[1:]:
		if ele > mmax:	mmax = ele
		if ele < mmin:	mmin = ele
	length = mmax - mmin + 1
	counts = [0]*length
	for ele in nums:
		counts[ele-mmin] += 1
	pos = 0
	for i in range(length):
		for j in range(counts[i]):
			nums[pos] = mmin + i
			pos+=1
import numpy as np
nums = np.random.permutation(10)
print(nums)
countSort(nums)
print(nums)