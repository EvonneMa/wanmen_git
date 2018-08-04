# 寻找逆序对
# 统计排序过程中的交换次数
# 相比之下归并排序既合适又快速
def countInverse(nums,start,end):
	if len(nums) < 2:
		return 0
	if end - start == 0:
		return [nums[end]],0
	if end - start == 1:
		if nums[end] < nums[start]:
			return [nums[end],nums[start]],1
		else:
			return [nums[start],nums[end]],0
	mid = start + (end - start) // 2
	left,l_num = countInverse(nums,start,mid)
	right,r_num = countInverse(nums,mid + 1,end)
	i = 0
	j = 0
	ans = []
	num = l_num + r_num
	while(i < mid - start + 1 and j < end - mid):
		if right[j] < left[i]:
			num += mid - i + 1
			ans.append(right[j])
			j += 1
		else:
			ans.append(left[i])
			i += 1
	if i == mid - start + 1:
		ans += right[j:]
	if j == end - mid:
		ans += left[i:]
	return ans,num	
nums = [2,4,1,3,5]
print(countInverse(nums,0,len(nums) - 1))
			