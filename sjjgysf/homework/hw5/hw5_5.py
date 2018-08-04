# 搜索区间
def findSection(nums,tar,start0,end0):
	if len(nums) == 0:
		return (-1,-1)
	# 寻找第一个
	start = start0
	end = end0
	while end - start > 1:
		mid = start + (end - start) //2
		if nums[mid] == tar:
			end = mid
		elif nums[mid] > tar:
			end = mid - 1
		else:
			start = mid + 1
	if nums[start] == tar:
		a = start
	elif nums[end] == tar:
		a = end
	else:
		a = -1
		return (-1,-1)
	# 寻找最后一个
	start = start0
	end = end0
	while end - start > 1:
		mid = start + (end - start) //2
		if nums[mid] == tar:
			start = mid
		elif nums[mid] > tar:
			end = mid - 1
		else:
			start = mid + 1
	if nums[end] == tar:
		b = end
	else:
		b = start
		
	return (a,b)
nums = [1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,3,3,4]
a,b = findSection(nums,2,0,len(nums) - 1)
print(a,b) 