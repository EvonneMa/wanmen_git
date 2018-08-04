def findZero(nums):
	if len(nums) == 0:
		return 0
	def findZerosHelper(nums,start,end):
		num = 0
		if end - start > 0:
			mid = start + (end - start) // 2
			num += findZerosHelper(nums,start,mid)
			num += findZerosHelper(nums,mid + 1,end)
			return num
		return int(nums[start] == 0)

	return findZerosHelper(nums,0,len(nums) - 1)
#nums = [1,0,0,1,0,0,0,0,2,0,33,0,4,5,6,0,0,4] #10
nums = [0,1,2,0,0,0,0,9,7,0,8,6,0] #7
#nums = [1]
#nums = []
print(findZero(nums))