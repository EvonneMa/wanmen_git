# ×ÖÄ¸¼ÆÊý
def letterCount(s):
	dic = {}
	for ch in s:
		if ch.isalpha():
			dic[ch] = dic.get(ch,0) + 1
	maxnum = 0
	maxch = ''		
	for k in list(dic.keys()):
			if dic[k] > maxnum:
				maxnum = dic[k]
				maxch = k
	print(maxnum,maxch)
s = 'Hello world, hehe hehe hehe hehe hehe'
letterCount(s)
	