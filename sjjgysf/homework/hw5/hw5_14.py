# 合并区间
# emmmmmm...似乎和二分没啥关系
def mergeSection(nums):
	nums.sort(key = lambda x:x[0])
	ans = [nums[0]]
	for ele in nums[1:]:
		if ele[0] <= ans[-1][1]:
			ans[-1][1] = max(ele[1],ans[-1][1])
		else:
			ans.append(ele)
	return ans
#nums = [[0, 9], [0, 1], [0, 2], [1, 9], [2, 5], [10, 11], [12, 20], [19, 20]]
#ans = mergeSection(nums)
#
def insertSection(nums,tar):
	ans = []
	flag = 1
	for ele in nums:
		if ele[1] >= tar[0] and ele[0] <= tar[1]:
			tar[0] = min(tar[0],ele[0])
			tar[1] = max(tar[1],ele[1])
			continue
		if ele[0] > tar[1] and flag:
			ans.append(tar)
			flag = 0
		ans.append(ele)
	return ans
nums = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16],[100,200]]
tar = [4,8]
ans = insertSection(nums,tar)
print(ans)
			
		
		