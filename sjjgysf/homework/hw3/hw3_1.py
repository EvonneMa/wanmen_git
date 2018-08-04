# ÇóºÍ
def qh(m):
	res = None
	if m == 1:
		return 1
	if res:
		return res
	res = m+qh(m-1)
	return res
n = 100
print(qh(n))