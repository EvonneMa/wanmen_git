# 寻找峰值
# O(lgn)
def getMountain(nums):
	if len(nums) == 1:
		return 0
	if nums[1] < nums[0]:
		return 0
	if nums[-2] < nums[-1]:
		return len(nums)-1
	start = 1
	end = len(nums) - 2
	while(end - start > 1):
		mid = start + (end - start) // 2
		if nums[mid] > nums[mid - 1]:
			if nums[mid] > nums[mid + 1]:
				return mid
			else:
				start = mid + 1
				continue
		else:
			end = mid - 1
			continue
	if nums[start] > nums[start - 1] and nums[start] > nums[start + 1]:
		return start
	return end
import numpy as np
nums = np.random.permutation(10)
print(nums)
print(nums[getMountain(nums)])