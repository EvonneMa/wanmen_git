# �ϲ�������������
def mergeList(head1,head2):
	a = head1.next
	b = head2.next
	head = c = Node(0) # �����½�һ������
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