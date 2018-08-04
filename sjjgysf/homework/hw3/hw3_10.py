# 指定字母大小写
# 我的思路：
#	1.对当前值判断(生成备选集合)
#	2.对是否继续递归进行判断
#	3.对当前值和递归结果进行组合(有些时候需要返回值,有些时候不需要、因而也就不需要组合了)
#
def char_permu(s,t):
	res = []
	if s[0] in t:
		a = [s[0],s[0].upper()]
	else:
		a = [s[0]]
	if len(s) == 1:
		return a
	b = char_permu(s[1:],t)
	for ele in a:
		for item in b:
			ele += item
			res.append(ele)
			ele = ele[0]
	return res
s ='sabersakura'
t = 'a,b'
print(char_permu(s,t))		