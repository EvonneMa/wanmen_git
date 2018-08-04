# 推荐类似写法,记住结构,注意利用好传址
# 可以与之前程序对比一下
# 对比给出的两种写法,学习一下
def findSubset(nums):
	res = []
	temp = []
	#findSubsetHelper_mine(nums,res,temp)
	findSubsetHelper_std(nums,res,temp,0)
	return res
def findSubsetHelper_std(nums,res,temp,n):
	res.append(temp[:])
	for i in range(n,len(nums)):
		temp.append(nums[i])
		findSubsetHelper(nums,res,temp,n+1)
		temp.pop()
def findSubsetHelper_mine(nums,res,temp):
	for i in range(2):
		if i:
			temp.append(nums[0])
		if len(nums) == 1:
			res.append(temp[:])
		else:
			findSubsetHelper(nums[1:],res,temp)
	temp.pop()
a = [1,2,3,4,5]
b = findSubset(a)
print(b,len(b))