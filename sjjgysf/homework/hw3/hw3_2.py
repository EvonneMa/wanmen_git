# �׳�
def jc(m):
	res = None
	if res:
		return res
	if m == 1:
		return 1
	res = m*jc(m-1)
	return res
m = 5
print(jc(m))