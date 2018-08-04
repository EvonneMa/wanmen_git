# 两数组交集
# set(需要输出重复数字时不可用)
# sort+bs
# sort+tp(双指针更灵活)——采用
# 关于复杂度的问题本题并不很明确,因此不详细优化
def findInner(nums1,nums2,DUPLI = False):
	nums1.sort()
	nums2.sort()
	i = j = 0
	res = []
	while(i < len(nums1) and j < len(nums2)):
		if not DUPLI:
			if i > 0:
				while(nums1[i] == nums1[i - 1]):
					i += 1
			if j > 0:
				while(nums2[j] == nums2[j - 1]):
					j += 1
		if nums1[i] == nums2[j]:
			res.append(nums1[i])
			i += 1
			j += 1
			continue
		if nums1[i] > nums2[j]:
			j += 1
			continue
		if nums1[i] < nums2[j]:
			i += 1
			continue
	return res
nums1 = [1,2,2,3,4,4,4,5]
nums2 = [1,1,3,4,4,5,7]
ans = findInner(nums1,nums2,DUPLI = True)
print(ans)