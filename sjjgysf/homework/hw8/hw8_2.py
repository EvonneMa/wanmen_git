# basketball score
def calScore(s):
	stack = []
	i = 0
	for ch in s:
		if ch == 'D':
			stack.append(stack[-1]*2)
			i += 1
		elif ch == '+':
			temp1 = stack.pop()
			temp2 = stack[-1]
			stack.append(temp1)
			stack.append(temp1+temp2)
			i += 1
		elif ch == 'C':
			stack.pop()
			i -= 1
		else:
			stack.append(int(ch))
			i += 1
	sums = 0
	while(i > 0):
		sums += stack.pop()
		i -= 1
	return sums
#s = ['5','2','C','D','+']
s = ['5','-2','4','C','D','9','+','+']
print(calScore(s))
		