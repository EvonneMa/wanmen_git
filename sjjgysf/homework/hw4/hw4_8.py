# 快速排序
# 最差情况下O(n^2),一般情况下O(nlgn)
# 参考元素的选取(pivot,即程序中的nums[start])
#	选择nums[0]、nums[mid]、nums[-1]的中位数会比较好
def quickSort(nums,start,end):
	if len(nums) < 2:
		return
	if end - start < 2:
		if nums[end] < nums[start]:
			temp = nums[end]
			nums[end] = nums[start]
			nums[start] = temp
		return 
	mid = start + (end - start) // 2
	temp = nums[mid]
	nums[mid] = nums[start]
	nums[start] = temp
	i = start + 1
	j = end
	while(True):
		while(i < end + 1 and nums[i] < nums[start]):
			i += 1
		while(j > start and nums[j] >= nums[start]):
			j -= 1
		if i >= j:
			break
		temp = nums[i]
		nums[i] = nums[j]
		nums[j] = temp
	temp = nums[j]
	nums[j] = nums[start]
	nums[start] = temp
	if j - start > 1:
		quickSort(nums,start,j - 1)
	if end - j > 1:
		quickSort(nums,j + 1,end)
import numpy as np
#nums = np.random.permutation(0)
#nums[4:6] = 100
#nums = [1, 3, 5, 7, 9, 2, 9,9,9, 0]
nums = [2,1]
quickSort(nums,0,len(nums)-1)
print(nums)