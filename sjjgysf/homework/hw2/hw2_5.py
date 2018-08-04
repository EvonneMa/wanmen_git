# 顺时针旋转数组
# 关键在于如何对应旋转前后的两个数组
matrix = [[20, 15, 10, 5, 0],
	[21, 16, 11, 6, 1],
	[22, 17, 12, 7, 2],
	[23, 18, 13, 8, 3],
	[24, 19, 14, 9, 4]]
def rotate(matrix):
	n = len(matrix)
	mid = n//2
	#res = [[0]*n for i in range(n)]
	for i in range(mid):
		start = i
		end = n-i-1
		for j in range(start,end):
			temp = matrix[i][j]
			matrix[i][j] = matrix[n-1-j][i]
			matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
			matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
			matrix[j][n-1-i] = temp
	return matrix
def show(matrix):
	n = len(matrix)
	for i in range(n):
		for j in range(n):
			print(matrix[i][j],end = '   ')
		print()
	print()			
show(matrix)
for i in range(4):
	matrix = rotate(matrix)
	show(matrix)

