import random
# compute pai
num = 100000000
ins = 0
for i in range(num):
	x = random.uniform(-1,1)
	y = random.uniform(-1,1)
	if x**2+y**2 <= 1:
		ins+=1
print(ins/num*4)