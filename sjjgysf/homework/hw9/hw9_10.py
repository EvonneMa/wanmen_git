# ���ַ���������ĸ���ִ�������
def reSort(s):
	dic = {}
	for ch in s:
		dic[ch] = dic.get(ch,0) + 1
	ans = []
	for k,v in dic.items():
		ans.append((k,v))
	ans.sort(key = lambda x:x[1],reverse = True)
	res = ''
	for k,v in ans:
		res += k*v

	print(res)
#s = "tree"
#s ="cccaaa"
s = "Aabb"
reSort(s)
		