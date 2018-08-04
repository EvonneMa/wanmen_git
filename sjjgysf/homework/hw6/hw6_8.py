# 子序列和最大
# 贼鸡儿经典
def maxSum2(nums,start,end):
	if len(nums) == 0:
		return -1
	if len(nums) == 1:
		return nums[0]

	if end - start > 1:
		mid = start + (end - start) // 2
		if mid - start > 0:
			lmax = maxSum2(nums,start,mid)
		else:
			lmax = nums[start]
		if end - mid - 1 > 0:
			rmax = maxSum2(nums,mid +1,end)
		else:
			rmax = nums[end]
		temp = nums[mid] + nums[mid + 1]
		mmax = temp
		for i in range(mid - 1,start - 1,-1):
			temp += nums[i]
			mmax = max(mmax,temp)
		temp = mmax 
		# 表示继承了左边的最大值
		for i in range(mid + 2,end + 1):
			temp += nums[i]
			mmax = max(mmax,temp)
	if end - start == 1:
		return max(nums[end],nums[start],nums[end] + nums[start])
	return max(lmax,rmax,mmax)
		
def maxSum1(nums):
	if len(nums) == 0:
		return -1
	if len(nums) == 1:
		return nums[0]
	temp = nums[0]
	ans = temp
	for ele in nums[1:]:
		temp = max(temp + ele,ele)
		ans = max(ans,temp)
		# 如果ans已经是负数,就没必要再累计了,直接另起一个就好
	return ans
nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums = [1,2,3,4,5]
print(maxSum2(nums,0,len(nums) - 1))