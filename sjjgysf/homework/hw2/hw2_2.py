# 矩阵0转换
matrix = [  [ 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
            [ 1, 1, 0, 1, 1, 1, 1, 1, 1, 1 ],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]
def zero_transform(matrix):
	pos = [[],[]]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 0:
				if i not in pos[0]:
					pos[0].append(i)
				if j not in pos[1]:
					pos[1].append(j)
	for x in pos[0]:
		for j in range(len(matrix[0])):
			matrix[x][j] = 0
	for y in pos[1]:
		for i in range(len(matrix)):
			matrix[i][y] = 0
	return matrix
ans = zero_transform(matrix)
for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		print(ans[i][j],end = '')
	print()