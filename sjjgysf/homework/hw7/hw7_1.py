# 合并两个有序链表
def mergeList(head1,head2):
	a = head1.next
	b = head2.next
	head = c = Node(0) # 代表新建一个链表
	while( a and b):
		if a.val > b.val:
			c.next = a
			c = c.next
			a = a.next
		else:
			c.next = b
			c = c.next
			b = b.next
	if a:
		c.next = a
	else:
		c.next = b
	return head