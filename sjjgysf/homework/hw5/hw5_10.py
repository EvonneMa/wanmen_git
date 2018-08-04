# 矩阵搜索
# 方法1：逐行二分,并且用判断缩小下一行的循环范围
# 方法2：从左下角开始,偏大向上、偏小向右
from bisect import bisect
def findNumInMatrix(matrix,tar):
	m = len(matrix)
	n = len(matrix[0])
	ans = []
	for i in range(m):
		if tar < matrix[i][0]:
			break
		pos = bisect(matrix[i][:n],tar)
		if pos:
			if matrix[i][pos - 1] == tar:
				ans.append([i,pos - 1])
			n = pos
		else:
			return -1
	return ans
matrix = [
    [1, 4, 8, 10,15],
    [3, 5, 16,17,20],
    [9, 20,22,24,29],
    [11,22,23,29,39]
]
print(findNumInMatrix(matrix,0))