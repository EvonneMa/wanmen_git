# 数字表达式
# 重要的还是数学思路
def exp(a,b):
	if a == b:
		return a
	if b%2 == 1 or b < 2*a:
		return '('+str(exp(a,b-1))+'+1)'
	return str(exp(a,int(b/2)))+'*2'
print(exp(11,113))