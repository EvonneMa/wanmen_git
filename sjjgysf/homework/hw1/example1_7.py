# 编码问题
def oneEnd(bits):
	'''
	遇到1向后移两位,遇到0向后移一位
	'''
	i = 0
	while i < len(bits) - 1:
		i += bits[i] + 1
	return i == len(bits) - 1 and bits[i] == 0
print(oneEnd([1,1,0,1,0]))