# 变位词
# 指给定一个单词s,如果s'是单词s所有字母的一种全排列,则s和s'互为变位词
from collections import Counter
def isAnagram(s,t):
	c = Counter(s)
	for ch in t:
		if ch not in c or t.count(ch) != c[ch]:
			return False
	return True
#s = "anagram"
#t = "nagaram"
s = "rat"
t = "car"
print(isAnagram(s,t))