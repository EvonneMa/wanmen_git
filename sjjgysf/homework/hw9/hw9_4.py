# 数组交集
from collections import Counter
def findIntersection(nums1,nums2):
	c1 = Counter(nums1)
	c2 = Counter(nums2)
	ans = []
	for ele in list(c1.keys()):
		if c2.get(ele,0):
			ans.extend([ele]*min(c2.get(ele,0),c1.get(ele,0)))
	print(ans)
nums1 = [1,2,2,1]
nums2 = [2,2]
findIntersection(nums1,nums2)