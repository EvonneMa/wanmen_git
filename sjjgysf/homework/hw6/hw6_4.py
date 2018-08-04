# 查找中值/第k小元素,未排序
# 快速排序来帮助选边站
def findKthLeastNum(nums,k):
	if len(nums) == 0:
		return -1
	if k > len(nums):
		return -1
	if len(nums) == 1:
		return nums[0]
	p = 0
	start = 1
	end = len(nums) - 1
	while(start <= end):
		i = start
		j = end
		while(True):
			while(i < end + 1 and nums[i] <= nums[p]):
				i += 1
			while(j > start - 1 and nums[j] > nums[p]):
				j -= 1
			if (j <= i):
				break
			temp = nums[i]
			nums[i] = nums[j]
			nums[j] = temp
		temp = nums[p]
		nums[p] = nums[j]
		nums[j] = temp
		print(nums)
		if j == k - 1:
			return nums[j]
		if j > k - 1:
			end = j - 1
		else:
			p = j + 1
			start = j + 2
	if p == k - 1:
		return nums[p]
	return nums[j]
import numpy as np
nums = np.random.permutation(10)
print(nums)
print(findKthLeastNum(nums,5))