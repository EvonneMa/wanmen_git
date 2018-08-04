## 二分搜索(返回tar第一次出现的位置)
def binSearch(nums,tar,start,end):
	if len(nums) == 0:
		return -1
	if end - start <= 1:
		if nums[start] == tar:
			return start
		elif nums[end] == tar:
			return end
		else:
			return -1
	mid = start+(end-start)//2 #如果采用(e+s)//2可能会导致e+s大于最大整数而报错
	if nums[mid] == tar:
		return binSearch(nums,tar,start,mid)
	elif nums[mid] < tar:
		return binSearch(nums,tar,mid+1,end)
	else:
		return binSearch(nums,tar,start,mid-1)
n = 10
tar = 2
nums = [1,2,2,3,6,8,7,2,4,2] 
nums.sort()
print(binSearch(nums,tar,0,n-1))

import unittest
class TestSequenceSearch(unittest.TestCase):
	def setUp(self):
		#self._f = sequenceSearch
		self._f = binSearch
	def test_empty(self):
		nums = []
		r = self._f(nums,5,0,len(nums)-1)
		self.assertEqual(-1,r)
	def test_one(self):
		nums = [1]
		r = self._f(nums,1,0,len(nums)-1)
		self.assertEqual(0,r)
		r = self._f(nums,2,0,len(nums)-1)
		self.assertEqual(-1,r)
	def test_tow(self):
		nums = [1,2]
		r = self._f(nums,1,0,len(nums)-1)
		self.assertEqual(0,r)
		r = self._f(nums,2,0,len(nums)-1)
		self.assertEqual(1,r)
		r = self._f(nums,11,0,len(nums)-1)
		self.assertEqual(-1,r)
	def test_more(self):
		nums = [1,2,3]
		r = self._f(nums,1,0,len(nums)-1)
		self.assertEqual(0,r)
		r = self._f(nums,3,0,len(nums)-1)
		self.assertEqual(2,r)
		r = self._f(nums,11,0,len(nums)-1)
		self.assertEqual(-1,r)
	def test_duplicate(self):
		nums = [1,2,2,3,3]
		r = self._f(nums,2,0,len(nums)-1)
		self.assertEqual(1,r)
		r = self._f(nums,11,0,len(nums)-1)
		self.assertEqual(-1,r)
unittest.main(argv = ['first-arg-is -ignored'],exit = False)