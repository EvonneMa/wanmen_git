# shuffle
import random
nums = []
n = 10
for i in range(n):
	nums.append(i+1)
for i in range(n):
	pos = random.randint(i,n-1)
	temp = nums[i]
	nums[i] = nums[pos]
	nums[pos] = temp
print(nums)