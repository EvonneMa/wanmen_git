# ���볡
def findDistance(nums):
	m = len(nums)
	n = len(nums[0])
	def bfs(i,j,nums,distance):
		a = [(i,j,0)]
		ptr = 0
		#direc = [[0,1],[0,-1],[1,0],[-1,0]]
		while(ptr < len(a)):
			ii,jj,step = a[ptr]
			if nums[ii][jj] == 0:
				distance[i][j] = step
				return
			if ii - 1 >= 0:
				a.append((ii - 1,jj,step + 1))
			if jj - 1 >= 0:
				a.append((ii,jj - 1,step + 1))
			if ii + 1 < m:
				a.append((ii + 1,jj,step + 1))
			if jj + 1 < n:
				a.append((ii,jj + 1,step + 1))
			ptr += 1
	distance = [[0]*n for _ in range(m)]
	for i in range(m):
		for j in range(n):
			if nums[i][j] == 0:
				continue
			bfs(i,j,nums,distance)
	print(distance)
nums = [[0,0,0],[0,1,0],[1,1,1]]
findDistance(nums)
	