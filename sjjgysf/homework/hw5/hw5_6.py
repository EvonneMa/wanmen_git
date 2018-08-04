# 在含有空格的字符串中寻找指定字符
# 最差情况为O(n),甚至可以用in,因为复杂度是一样的
def findCharWithSpace(nums,tar):
	if len(nums) == 0:
		return -1
	start = 0
	end = len(nums) - 1
	while(end - start > 1):
		while(end - start > 1) and nums[end] == '':
			end -= 1
		if nums[end] == '':
			end -= 1
		if end < start:
			return -1
		
		mid = start + (end - start) // 2
		while(nums[mid] == ''):
			mid += 1
			
		if nums[mid] == tar:
			return  mid
		elif nums[mid] > tar:
			end = mid - 1
		else:
			start = mid + 1
	
	if nums[end] == tar:
		return end
	if nums[start] == tar:
		return start
	return -1
nums = ['','',1,4,'',6,9,'','','','','','',12,'','','',66,'','','','','','',98,'','',]
print(findCharWithSpace(nums,66))