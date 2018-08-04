# 顺序搜索与二分搜索
def sequenceSearch(num,tar):
	for i in range(len(num)):
		if num[i] == tar:
			return i
	return -1
def binSearch(nums,tar):
	nums.sort()
	s = 0
	e = len(nums)-1
	while(s<=e):
		mid = s+(e-s)//2 #如果采用(e+s)//2可能会导致e+s大于最大整数而报错
		if nums[mid] == tar:
			return mid
		elif nums[mid] < tar:
			s = mid+1
		else:
			e = mid-1
	return -1
import unittest
class TestSequenceSearch(unittest.TestCase):
	def setUp(self):
		#self._f = sequenceSearch
		self._f = binSearch
	def test_empty(self):
		nums = []
		r = self._f(nums,5)
		self.assertEqual(-1,r)
	def test_one(self):
		nums = [1]
		r = self._f(nums,1)
		self.assertEqual(0,r)
		r = self._f(nums,2)
		self.assertEqual(-1,r)
	def test_tow(self):
		nums = [1,2]
		r = self._f(nums,1)
		self.assertEqual(0,r)
		r = self._f(nums,2)
		self.assertEqual(1,r)
		r = self._f(nums,11)
		self.assertEqual(-1,r)
	def test_more(self):
		nums = [1,2,3]
		r = self._f(nums,1)
		self.assertEqual(0,r)
		r = self._f(nums,3)
		self.assertEqual(2,r)
		r = self._f(nums,11)
		self.assertEqual(-1,r)
	def test_duplicate(self):
		nums = [1,2,2,3,3]
		r = self._f(nums,2)
		self.assertEqual(2,nums[r])
		r = self._f(nums,3)
		self.assertEqual(3,nums[r])
		r = self._f(nums,11)
		self.assertEqual(-1,r)
unittest.main(argv = ['first-arg-is -ignored'],exit = False)