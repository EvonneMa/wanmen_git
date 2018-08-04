# 找到当前数字之后比该数字小的数字个数
# 使用插入排序,O(n^2)
def findNum(nums):
	ans = {}
	i = 1
	while(i < len(nums)):
		cnt = i
		temp = cnt - 1
		while(temp > -1):
			if nums[cnt] < nums[temp]:
				ans[nums[temp]] = ans.get(nums[temp],0) + 1
				a = nums[temp]
				nums[temp] = nums[cnt]
				nums[cnt] = a
				cnt -= 1
				temp -= 1
			else:
				temp -= 1
		i += 1
	for i in nums:
		if i in ans:
			print(i,ans[i])
		else:
			print(i,0)
import numpy as np
nums = np.random.permutation(10)
print(nums)
findNum(nums)