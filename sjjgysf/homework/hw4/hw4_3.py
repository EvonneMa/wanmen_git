# 选择排序
def selectSort(nums):
	length = len(nums)
	for i in range(length-1):
		minimum = float('inf')
		idx = None
		for j in range(i+1,length):
			if nums[j] < min(nums[i],minimum):
				idx = j
				minimum = nums[j]
		if idx:
			temp = nums[i]
			nums[i] = nums[idx]
			nums[idx] = temp
import numpy as np
nums = np.random.permutation(10)
selectSort(nums)
print(nums)