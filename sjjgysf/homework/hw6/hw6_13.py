# 奇偶排序
# 一边分、一边治
def sortByIndex(nums,start,end):
	if end - start < 2:
		return
	mid = start + (end - start) // 2
	a = start + (mid - start) // 2 + 1
	b = mid + 1 - a
	for i in range(a,mid + 1):
		temp = nums[i]
		nums[i] = nums[i + b]
		nums[b + i] = temp
	#print(nums)
	sortByIndex(nums,start,mid)
	sortByIndex(nums,mid + 1,end)
def prepro(nums):
	length = len(nums)
	i = 2
	while(i < length):
		i*=2
	nums = nums[:length//2] + [-1]*((i-length) // 2) + nums[length // 2:] + [-1]*((i-length) // 2)
	sortByIndex(nums,0,i-1)
	return nums[:length]
nums = [1,2,3,4,5,6,7,8,9,10]
ans = prepro(nums)
print(ans)