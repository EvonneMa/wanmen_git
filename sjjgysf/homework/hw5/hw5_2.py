# 旋转数组最小值
# 查找：
def findMin(nums,start,end):
	if len(nums) == 0:
		return -1
	if nums[0] < nums[end]:
		return nums[0]
	if start == end:
		return nums[end]
	mid = start + (end - start) // 2
	if nums[mid] >= nums[0]:
		return findMin(nums,mid + 1,end)
	else:
		return findMin(nums,start,mid)
nums = [3,4,5,6,7,1,1,1,2,3]
print(findMin(nums,0,len(nums)-1))