# 将有序数组转化为一颗平衡树
# 有序链表也一样
import BST
nums = [-10,-3,0,5,9]
def getTree(nums):
	if len(nums) == 0:
		return None
	mid = len(nums) // 2
	root = BST.Node(nums[mid])
	root.left = getTree(nums[:mid])
	root.right = getTree(nums[mid+1:])
	return root
s = BST.BST(getTree(nums))
s.inloop()
s.postloop()
s.preloop()