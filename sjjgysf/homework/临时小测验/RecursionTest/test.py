def letterCase(nums,tar,start,k):
	if not k:
		return nums[start:]
	res = ''
	while(nums[start] != tar):
		res += nums[start]
		start += 1
		
	res += nums[start].upper()
	res += letterCase(nums,tar,start + 1,k - 1)
	return res
nums = 'love you and love me,yoooooooooooooo'
print(letterCase(nums,'o',0,7))