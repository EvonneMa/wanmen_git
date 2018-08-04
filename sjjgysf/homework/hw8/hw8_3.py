# 星球大战
def starWar(nums):
	stack = []
	
	for ele in nums:
		if stack == []:
			stack.append(ele)
			continue
		if ele == 0:
			continue
		if ele*stack[-1] > 0 or stack[-1] < 0:
			stack.append(ele)
		else:
			while(len(nums) > 0 and abs(ele) > stack[-1] and ele*stack[-1] < 0):
				stack.pop()
			if len(nums) == 0 or ele*stack[-1] > 0:
				stack.append(ele)
	return stack
#nums = [5,10,-5]
#nums = [10,2,-5]
nums = [-2,-1,1,2]
print(starWar(nums))
				
					