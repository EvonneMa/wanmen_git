# 寻找子集——回溯算法
# a[:]生成一个a的copy
def get_sub(n):
	if len(n) == 1:
		return [[],[n[0]]]
	res = []
	temp = [[n[0]],[]]
	
	for ele in temp:
		
		ans = get_sub(n[1:])
		#print(ans,len(n))
		for item in ans:
			c = ele.copy()
			c.extend(item)
			res.append(c)
	#print(res,len(n))
	return res
def pre_deal(nums):
	a = list(set(nums))
	a.sort()
	res = get_sub(a)
	return res
	
nums = [1,2,3,4,4,3,5,8,7,9,7,8,6,6,6]
ans = sorted(pre_deal(nums))
print(ans,len(ans))