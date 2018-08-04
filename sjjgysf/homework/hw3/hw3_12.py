# 括号对
def kuohao(n):
	res = []
	temp = []
	kuohaoHelper(temp,res,n)
	return set(res)
def kuohaoHelper(temp,res,n):
	for i in range(len(temp)+1):
		temp.insert(i,'(')
		for j in range(i+1,len(temp)+1):
			temp.insert(j,')')
			if n == 1:
				res.append(''.join(temp[:]))
			else:
				kuohaoHelper(temp,res,n-1)
			temp.pop(j)
		temp.pop(i)
n = 2
ans = kuohao(n)
print(ans)