# 供暖半径问题
# 本题的关键在于如何将思路引导到二分上面来
# 或者说：培养二分思想
# 其实就是每一间房屋能够在供暖设备序列中放在哪里,也就是findOrInsert()
# 寻找每一间房需要的最短半径,再取最大值
def findRadium(nums1,nums2):
	# O(mlgn)
	def findOrInsert(nums2,tar):
		'''
		from bisect import bisect
		可直接调用bisect
		'''
		start = 0
		end = len(nums2) - 1
		while(end - start > 1):
			mid = start + (end - start) // 2
			if nums2[mid] == tar:
				return 0
			elif nums2[mid] > tar:
				end = mid - 1
			else:
				start = mid + 1
		if nums2[start] >= tar:
			return nums2[start] - tar
		if nums2[end] > tar:
			return min(tar - nums2[start],nums2[end] - tar)
		return tar - nums2[end]
	if len(nums1) == 0:
		return 0
	if len(nums2) == 0:
		return float('inf')
	max_redium = 0
	nums2.sort()
	for tar in nums1:
		max_redium = max(max_redium,findOrInsert(nums2,tar))
	return max_redium
nums1 = [1,2,3,4]
nums2 = [1,4]
print(findRadium(nums1,nums2))
