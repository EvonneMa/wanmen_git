#-*-coding:GBK -*-
# 扫雷
import random
def gen_map(m,n,p):
	bomb_map = []
	number_map = []
	for i in range(m):
		bomb_map.append([None]*n)
		number_map.append([0]*n)
	# 生成地图完毕	
	direction = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]	
	for i in range(m):	
		for j in range(n):
			if(random.random()<p):
				bomb_map[i][j] = '*'
				number_map[i][j] = '*'
				for ele in direction:
					x = i+ele[0]
					y = j+ele[1]
					if x > -1 and x < m and y > -1 and y < n and number_map[x][y] != -1 and number_map[x][y] != '*':
						number_map[x][y] += 1
			else:
				bomb_map[i][j] = '.'
	for i in range(m):
		for j in range(n):
			print(bomb_map[i][j],end = '')
		print()
	for i in range(m):
		for j in range(n):
			print(number_map[i][j],end = '')
		print()
gen_map(7,7,0.3)			
	# 生成地图完毕
	
			