# 归并排序 分治算法
# 分治算法 + 递归 ~~~
# O(nlgn)
def cutMergeSort(nums,n):
	mid = n//2-1
	pos = []
	start = 0
	end = n-1
	def cut(nums,mid,start,end):
		if end - start < 2:
			if nums[start] > nums[end]:
				temp = nums[start]
				nums[start] = nums[end]
				nums[end] = temp
			return
		cut(nums,start + (mid + 1 - start)//2 - 1,start,mid)
		cut(nums,mid	 + (end - mid)//2,mid + 1,end)
		temp = []
		s1 = start
		s2 = mid + 1
		e1 = mid
		e2 = end
		while(s1 <= e1 and s2 <= e2):
			if nums[s1] <= nums[s2]:
				temp.append(nums[s1])
				s1 += 1
			else:
				temp.append(nums[s2])
				s2 += 1
		if s1 > e1:
			temp.extend(nums[s2:e2 + 1])
		else:
			temp.extend(nums[s1:e1 + 1])
		for i in range(len(temp)):
			nums[start + i] = temp[i]
	cut(nums,mid,start,end)
#nums = [170, 45, 75, 90, 802, 24, 2, 66]
#nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
import numpy as np
n = 10
nums = np.random.permutation(10)
print(nums)
cutMergeSort(nums,n)
print(nums)