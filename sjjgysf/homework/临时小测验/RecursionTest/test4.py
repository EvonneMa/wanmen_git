def reverseString(strs,i):
	if i > len(strs) - 1:
		return ''
	res = strs[i]
	return reverseString(strs,i+1) + res
print(reverseString('hello world and cnm',0))