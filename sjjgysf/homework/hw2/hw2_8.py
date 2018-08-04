# 寻找最大数字
def find_num(s):
	if s[0] > s[1]:
		m1,m2 = s[0],s[1]
		pos = 0
	else:
		m1,m2 = s[1],s[0]
		pos = 1
	for i in range(2,len(s)):
		if s[i] > m1:
			m2 = m1
			m1 = s[i]
			pos = i
		elif s[i] > m2:
			m2 = s[i]
	if m1 > m2*2:
		return pos
	else:
		return -1
nums = [1, 2,3,8,3,2,1]
print(find_num(nums))