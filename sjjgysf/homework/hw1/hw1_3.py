# 喝酒概率问题
import random
def drink():
	a = [False]*6
	cnt = 0
	while(True):
		pos = random.randint(0,5)
		if a[pos]:
			a[pos] = False
		else:
			a[pos] = True
		cnt += 1
		if sum(a) == 6:
			break
	return cnt
ans = 0
for j in range(10):
	for i in range(100000):
		ans += drink()
	print(ans/(i+1)/(j+1))