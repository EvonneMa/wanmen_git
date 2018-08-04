# 插入排序
# 由于每插入一个数字后都是有序的,因此速度会较冒泡和选择快
def insertSort(nums,n):
	for i in range(1,n):
		pos = i
		for j in range(i-1,-1,-1):
			if nums[j] > nums[pos]:
				temp = nums[pos]
				nums[pos] = nums[j]
				nums[j] = temp
				pos = j
import numpy as np
n = 10
nums = np.random.permutation(n)
print(nums)
nums[4:8] = 100
insertSort(nums,n)
print(nums)
	