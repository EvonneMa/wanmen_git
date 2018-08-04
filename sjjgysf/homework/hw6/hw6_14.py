# 最少步数拿硬币
# 找到最小值，根据最小值将数组分割,递归进行下去
def findMinStep(nums,start,end,h):
	if start == end:
		return 1
	if start > end:
		return 0
	k = start
	for i in range(start + 1,end + 1):
		if nums[i] < nums[k]:
			k = i
	a1 = findMinStep(nums,start,k - 1,nums[k])
	a2 = findMinStep(nums,k + 1,end,nums[k])
	return min(end - start + 1,a1 + a2 + nums[k] - h)
nums = [2,1,2,5,1]
print(findMinStep(nums,0,len(nums) - 1,0))