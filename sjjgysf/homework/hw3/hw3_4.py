# 打印尺子(画出来就像一根尺子)
# 递归很容易形成二叉树,因此必须警惕(比如这里如果不用ans保存结果而是用print_ruler(m-1),那就凉了)
def print_ruler(m):
	if m == 1:
		return [1]
	ans = print_ruler(m-1)
	res = []
	res.extend(ans)
	res.append(m)
	res.extend(ans)
	return res
m = 4
print(print_ruler(m))