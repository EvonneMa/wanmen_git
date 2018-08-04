# 找到所有anagram
# 可以考虑不用import,像队列一样处理
import hw9_8 as pre
def findAllAnagram(s,t):
	res = []
	length = len(t)
	for i in range(len(s) - length + 1):
		if pre.isAnagram(s[i:i+length],t):
			res.append(i)
	print(res)
#s = "cbaebabacd"
#t = "abc"
s = "abab" 
t = "ab"
findAllAnagram(s,t)