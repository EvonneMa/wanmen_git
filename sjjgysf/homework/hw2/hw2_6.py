#  反转字符串
def reverse_char(s):
	length = len(s) 
	mid = length//2
	res = ''
	for i in range(length-1,-1,-1):
		res += s[i]
	return res
s = 'sakuraemisagi'
print(reverse_char(s))