# 旋转数组指定值
# 查找：
def findMin(nums,start,end,tar):
	if len(nums) == 0:
		print( -1)
		return
	if start > end:
		print(-1)
		return
	if end == start:
		if tar == nums[start]:
			print(start)
			return
		else:
			print(-1)
			return
	mid = start + (end - start) // 2
	if nums[mid] == tar:
		print(mid)
		return
	else:
		if nums[mid] >= nums[0]:
			if tar > nums[mid] or tar < nums[0]:
				findMin(nums,mid + 1,end,tar)
			else:
				findMin(nums,start,mid - 1,tar)
		else:
			if tar > nums[mid] and tar < nums[0]:
				findMin(nums,mid + 1,end,tar)
			else:
				findMin(nums,start,mid - 1,tar)
nums = [3,4,5,6,7,1,2]
findMin(nums,0,len(nums)-1,1)