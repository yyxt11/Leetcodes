# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p1,p2 = head,head
        count = 0
        while(p1):
            p1 = p1.next
            count += 1

            if count == 2:
                p2 = p2.next
                count = 0
    

        return p2

    
            
