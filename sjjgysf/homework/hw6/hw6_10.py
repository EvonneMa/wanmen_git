# 多项式乘法
# 幂次缺失的用0代替
def multiPoly(res,nums1,nums2,mi1,mi2):
	if len(nums1)  == 0 and len(nums2) == 0:
		res = [1,2]
	else:
		start,end = prepro(nums1,nums2)
		print(start,end)
		if start >= end:
			print('mi = ',mi1,mi2,nums1[start]*nums2[start])
			res[mi1 + mi2] += nums1[start]*nums2[start]
			return
		mid = start + (end - start) // 2
		multiPoly(res,nums1[start:mid + 1].copy(),nums2[start:mid + 1].copy(),mi1 + start,mi2 + start)
		multiPoly(res,nums1[mid + 1:end + 1].copy(),nums2[mid + 1:end + 1].copy(),mi1 + mid + 1,mi2 + mid + 1)
		multiPoly(res,nums1[start:mid + 1].copy(),nums2[mid + 1:end + 1].copy(),mi1 + start,mi2 + mid + 1)
		multiPoly(res,nums1[mid + 1:end + 1].copy(),nums2[start:mid + 1].copy(),mi1 + mid + 1,mi2 + start)
	
def prepro(nums1,nums2):
	length1 = len(nums1)
	length2 = len(nums2)
	start = 0
	if length1 >= length2:
		nums2 += [0]*(length1 - length2)
		end = length1 - 1
	else:
		nums1 += [0]*(length2 - length1)
		end = length2 - 1
	return start,end
nums1 = [1,2,3,4,5,6,7]
nums2 = [1,2,3]
length1 = len(nums1)
length2 = len(nums2)
length = max(length1,length2) - 1
res = []
for i in range(length*length + 2):
	res.append(0)
multiPoly(res,nums1,nums2,0,0)
res = res[:length1 + length2 - 1]
if res:
	strs = ''
	for i in range(length1 + length2 - 2,-1,-1):
		if res[i]:
			if i:
				strs += str(res[i]) +'x^' + str(i) + '+'
			else:
				strs += str(res[i])
print(strs)
from numpy import convolve
print(convolve(nums1,nums2))
print(res)		