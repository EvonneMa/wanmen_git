# 森林中的兔子
def findMinRabbit(nums):
	from collections import Counter
	c = Counter(nums)
	#print(c)
	ans = 0
	for k,v in c.items():
		if v%(k+1):
			ans += (v // (k+1) + 1)*(k + 1)
		else:
			ans += v
			
	print(ans)
nums = [1,1,2]
#nums =  [10, 10, 10]
findMinRabbit(nums)