# �������ű���ʽ
def decodeString(strs):
	stack = []
	stack.append(['',1])
	num = ''
	for ch in strs:
		if ch.isdigit():
			num += ch
		elif ch == '[':
			stack.append(['',int(num)])
			num = ''
		elif ch == ']':
			a,b = stack.pop()
			stack[-1][0] += a*b
		else:
			stack[-1][0] += ch
	return stack[0][0]
print(decodeString('2[abc]3[bc]df'))