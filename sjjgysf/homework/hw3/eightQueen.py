# 八皇后问题
def eightQueen(matrix,n,num):
	#print(num)
	#print(matrix)
	if num == n:
		return True
	for i in range(n):
		for j in range(n):
			if num == 0:
				print(i,j)
			if isPossible(i,j,matrix,n):
				matrix[i][j] = False
				if eightQueen(matrix,n,num+1):
					return True
				matrix[i][j] = True
def isPossible(i,j,matrix,n):
	for idx in range(n):
		direction = [[i+idx,j+idx],[i+idx,j-idx],[i-idx,j+idx],[i-idx,j-idx]]
		if not(matrix[i][idx] and matrix[idx][j]):
			return False
		for ele in direction:
			if ele[0] > -1 and ele[0] < n and ele[1] > -1 and ele[1] < n:
				if not(matrix[ele[0]][ele[1]] ):
					return False
	return True
num = 0
n = 8
matrix = [[True]*n for i in range(n)]
if eightQueen(matrix,n,num):
	for i in range(n):
		print(matrix[i])


