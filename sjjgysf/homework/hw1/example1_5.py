import random
# ��ȡ���ٴβ��ܳ�����л�ɫ
def coupon(n):
	found = [False]*n
	counts = 0
	distinct = 0
	while(distinct<n):
		pos = random.randint(0,n-1)
		if not found[pos]:
			distinct +=1
			found[pos] = True
		counts += 1
	return counts
ans = 0
for i in range(10000):
	ans += coupon(10)
print(ans/i)