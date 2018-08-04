# 寻找重复数
# m = n//2,遍历寻找重复数在哪一侧;根据结果更新m,相当于对m进行二分查找
# O(nlgn)
# 重复数意味着有相同的入口,也就意味着成环,故可以用双指针法
def findDupliNum(nums,n):
	start = 1
	end = n
	while(end > start):
		mid = start + (end - start) // 2
		cnt = 0
		flag = 0
		for ele in nums:
			if ele <= mid:
				cnt += 1
			if ele == mid:
				flag += 1
				if flag > 1:
					return mid
		if cnt == mid:
			start = mid + 1
		else:
			end = mid - 1
	return start
#nums = [1,2,2,3,4,5,6,7,8,9]
nums = [3,5,6,3,1,4,2]	
print(findDupliNum(nums,9))