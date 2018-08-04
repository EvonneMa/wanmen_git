# 汉诺塔
# 整体思路是
#	借助C实现A->B
#	A->C
#	借助A实现B->C
def hnt(A,B,C,n):
	if n == 1:
		print('From '+A+' to '+C)
		return
	hnt(A,C,B,n-1)
	print('From '+A+' to '+C)
	hnt(B,A,C,n-1)
	return
hnt('A','B','C',3)