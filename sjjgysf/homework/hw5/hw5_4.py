## 搜索插入指定元素
# python bisect
def searchAndInsert(nums,tar,start,end):
	if len(nums) == 0:
		return 0
	if end - start > 1:
		mid = start + (end - start) // 2
		if nums[mid] == tar:
			return mid
		if nums[mid] > tar:
			return searchAndInsert(nums,tar,start,mid - 1)
		else:
			return searchAndInsert(nums,tar,mid + 1,end)
		
	if nums[start] >= tar:
		return start
	if nums[end] < tar:
		return end + 1
	if nums[end] >= tar:
		return end
nums = [1,3,5,7,9,11,13]
print(searchAndInsert(nums,6,0,len(nums)-1))

#
#if nums[start] >= tar:
#		return start
#	if nums[end] >= tar:
#		return end
#	return end + 1