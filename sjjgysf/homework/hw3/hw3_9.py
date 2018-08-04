# 全排列
def permutation(s,k):
	if len(s) == 1:
		return s
	ans = []
	for i in range(len(s)):
		res = s[i]
		
		if k-1 > 0:
			ss = s[0:i]+s[i+1:]
		#print(ss)
			
			temp = permutation(ss,k-1)
			for ele in temp:
				res += ele
				ans.append(res)
				res = res[0]
		else:
			ans.append(res)
	return ans
s = 'Hello'
k = 5
ans = permutation(s,k)
print(ans,len(ans))