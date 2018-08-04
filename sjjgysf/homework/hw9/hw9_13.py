# 砖墙
from collections import Counter
def brickWall(nums):
	ans = []
	rec = []
	for ele in nums:
		temp = []
		sums = 0
		for item in ele[:-1]:
			sums += item
			temp.append(sums)
		ans.extend(temp)
		rec.append(temp)
	#print(rec)
	c = Counter(ans)
	#print(c.items())
	pos = c.most_common(1)
	#print(pos)
	return len(nums) - pos[0][1]
nums = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
print(brickWall(nums))
			
		