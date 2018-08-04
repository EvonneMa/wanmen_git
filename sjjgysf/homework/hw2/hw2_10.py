# 相当于模拟了大数加法
def plus1(s):
	n = len(s)
	a = 1
	for i in range(-1,-n-1,-1):
		temp = a+s[i]
		if temp < 10:
			s[i] = temp
			return s
		else:
			s[i] = temp-10
			a = 1
	res = [1]
	#print(res)
	#print(s)
	res.extend(s)
	#print(res)
	return res
#s = [9, 9, 9]
s = [1,3,5,6,7,8,2,4]
print(plus1(s))