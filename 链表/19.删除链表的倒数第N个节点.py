#链表基础题，利用双指针一次遍历
# Definition for singly-linked list.

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        dumppointer = head

        if dumppointer is None or dumppointer.next is None:
            return None

        qucikpointer = dumppointer
        slowpointer = None

        gap = 0
        while(qucikpointer.next is not None):
            qucikpointer = qucikpointer.next
            gap += 1
            
            if gap > n - 1 :
                if slowpointer is None:
                    slowpointer = dumppointer
                else:
                    slowpointer = slowpointer.next

        if slowpointer is None:
            return dumppointer.next
        else:
            slowpointer.next = slowpointer.next.next

            return dumppointer

    
            
