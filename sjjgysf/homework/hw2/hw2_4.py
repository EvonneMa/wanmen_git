# sudoku
# 如何在一次循环内同时解决一行、一列和一小块
matrix = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]
def check_sudoku(matrix):
	n = len(matrix)
	
	for i in range(n):
		row = col = box = 0
		for j in range(n):
			# 行
			temp = matrix[i][j]
			if ((row & (1<<(temp-1))) == 0):
				row = row | (1<<(temp-1))
			else:
				return False
			# 列
			temp = matrix[j][i]
			if ((col & (1<<(temp-1))) == 0):
				col = col | (1<<(temp-1))
			else:
				return False
			# 分块
			sub_row = (i//3)*3 + j//3
			sub_col = i%3*3 + j%3
			temp = matrix[sub_row][sub_col]
			if ((box &(1<<(temp-1))) == 0):
				box = box | (1<<(temp-1))
			else:
				return False
	return True
print(check_sudoku(matrix))