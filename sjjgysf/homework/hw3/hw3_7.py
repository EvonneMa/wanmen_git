# ������(���ӵ�·�ź�)
# ���Կ���һ�±�����
def grayCode(n,forward):
	if n == 0:
		return
	grayCode(n-1,True)
	print('enter '+str(n) if forward else 'exit '+str(n))
	grayCode(n-1,False)
grayCode(4,True)