def findMin(nums):
	def findMinHelper(nums,start,end):
		if end - start > 1:
			i = start + 1
			j = end
			while(True):
				while(i < end + 1 and nums[i] < nums[start]):
					i += 1
				while(j >= start and nums[j] > nums[start]):
					j -= 1
				if (i >= j):
					break
				temp = nums[i]
				nums[i] = nums[j]
				nums[j] = temp
			temp = nums[start]
			nums[start] = nums[j]
			nums[j] = temp
			#print(nums)
			return findMinHelper(nums,start,j - 1)
		else:
			if nums[start] > nums[end]:
				return nums[end]
			else:
				return nums[start]
	return findMinHelper(nums,0,len(nums)-1)
import numpy as np
ans = []
for i in range(100):
	nums = np.random.permutation(10)
	#print(nums)
	ans.append(findMin(nums))
print(sum(ans))