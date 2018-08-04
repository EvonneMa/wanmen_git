# Any Sums
# 注意：既可以带有返回值(就像之前做的那样),这样需要多建立一个变量接收结果
#		也可以不带返回值,这样需要传参时多传递一个参数
def sums(tar,nums):
	temp = []
	res = []
	sumsHelper(tar,temp,res,nums,0)
	return res
def sumsHelper(tar,temp,res,nums,total):
	for i in range(len(nums)):
		if nums[i] in temp: continue 
		# 此处也可以用提前排序进行替换
		if total + nums[i] == tar:
			temp.append(nums[i])
			res.append(temp[:])
			temp.pop()
		elif total + nums[i] < tar:
			temp.append(nums[i])
			sumsHelper(tar,temp,res,nums[i+1:],total+nums[i])
			# 防止重复
			temp.pop()
tar = 7
nums = [2,2,3,7]
ans = sums(tar,nums)
print(ans)