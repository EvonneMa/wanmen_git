# 无限序列中寻找某元素第一次出现的位置,即无限长度的数据流
# start = 0,end = 1开始搜索,找不到便倍增区间,找到后转二分
def findEleInStream(nums,tar):
	start = 0
	end = 1
	while(nums[end] < tar):
		start = end + 1
		end *= 2
	return(findFirstPos(nums,tar,start,end))
def findFirstPos(nums,tar,start,end):
	while(end - start > 1):
		mid = start + (end - start) // 2
		if nums[mid] == tar:
			end = mid
		elif nums[mid] < tar:
			start = mid + 1
		else:
			end = mid - 1
	if nums[start] == tar:
		return start
	if nums[end] == tar:
		return end
	return -1
nums = [1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,6,7,8,9]
print(findEleInStream(nums,4))