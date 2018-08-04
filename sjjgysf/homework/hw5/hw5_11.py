# 矩阵搜索2：寻找第k个最小的数
# 每次取当前最大、最小值的一般进行逐行二分插入,根据插入位置缩小范围
from bisect import bisect
def findKthMin(matrix,k):
	start = matrix[0][0]
	end = matrix[-1][-1]
	while(end - start > 1):
		flag = 0
		pos = 0
		mid = start + (end - start) // 2
		for row in matrix:
			pos += bisect(row,mid)
			if pos >= k:
				end = mid # 大于等于k都有可能对,因为重复
				flag = 1
				break
		if flag:
			continue
		start = mid + 1 # 小于k一定不对
	for row in matrix:
		pos += bisect(row,start)
	if pos == k:
		return start
	return end
matrix = [
    [1, 4, 8, 10,15],
    [3, 5, 16,17, 20],
    [9, 20,22,24,29],
    [11,22,23,29,39]
]
k = 5
print(findKthMin(matrix, k))