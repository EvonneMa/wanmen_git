# Hadamard matrix

def gen_hadamard(matrix,m):
	if m == 1:
		matrix = [[matrix[0]]]
	for i in range(m):
		temp = []
		for ele in matrix[i]:
			temp.append(ele)
		matrix[i].extend(temp)
		temp = []
		for ele in matrix[i]:
			temp.append(ele)
		matrix.append(temp)
		for i in range(m,m*2):
			matrix[-1][i] *= -1
	return 2*m,matrix
H = [1]
m = 1
times = 4
for i in range(times):
	m,H = gen_hadamard(H,m)
print(H)