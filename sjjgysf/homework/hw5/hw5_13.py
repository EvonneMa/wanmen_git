# 两个有序数组的中值
from bisect import bisect
def findMinInTwoArr(nums1,nums2,n1,n2):
	start = min(nums1[0],nums2[0])
	end = max(nums1[n1-1],nums2[n2-1])
	tar = n1 + (n2 - n1) // 2
	while(start < end):
		mid = start + (end - start) // 2
		k1 = bisect(nums1,mid)
		k2 = bisect(nums2,mid)
		if k1 + k2 > tar:
			end = mid
		elif k1 + k2 < tar:
			start = mid + 1
		else:
			break
	if k1 >= n1:
		return nums2[k2]
	if k2 >= n2:
		return nums1[k1]
	return min(nums1[k1],nums2[k2])
n1 = 10
n2 = 3
nums1 = [1,2,2,2,2,2,7,8,9,10]
nums2 = [1,2,3]
import numpy as np
#nums1 = np.array([1,2,3,4,5,6,7,8,9,10])
#nums1 *= 100
#nums2 = [11,22,33]
#nums2 = [11,220,3300]
print(findMinInTwoArr(nums1,nums2,n1,n2))