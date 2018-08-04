# 寻找多余元素
# 与二分法结合
def findExtraEle(nums1,nums2,start,end):
	if end == 0:
		return nums1[0]
	while(end - start > 1):
		mid = start + (end - start) // 2
		if nums1[mid] == nums2[mid]:
			start = mid + 1
		else:
			end = mid
	if nums1[start] == nums2[start]:
		return nums1[end]
	return nums1[start]
nums1 = [1,2,3,4,5,99,888]
nums2 = [1,2,3,4,5,888]
print(findExtraEle(nums1,nums2,0,len(nums2) - 1))