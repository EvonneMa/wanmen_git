# 九宫格
# 最后一行的中间放1,同时向右向下移动一格,依次摆放
# 如果有数,从最新的数字上方开始继续放
def gen(n):
	ans = [[0]*n for i in range(n)]
	x = n-1
	y = int(n/2)
	for i in range(n*n):
		if x > n-1:
			x = 0
		if y > n-1:
			y = 0
		if ans[x][y] != 0:
			x -= 2
			y -= 1
		ans[x][y] = i+1
		x += 1
		y += 1
	for i in range(n):
		for j in range(n):
			print(ans[i][j],end = '  ')
		print()
gen(5)
	