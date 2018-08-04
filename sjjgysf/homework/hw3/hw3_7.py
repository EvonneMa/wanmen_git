# 格雷码(电子电路信号)
# 可以考虑一下变形题
def grayCode(n,forward):
	if n == 0:
		return
	grayCode(n-1,True)
	print('enter '+str(n) if forward else 'exit '+str(n))
	grayCode(n-1,False)
grayCode(4,True)