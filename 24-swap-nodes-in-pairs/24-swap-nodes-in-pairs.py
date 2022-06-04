# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        d = ListNode(0)
        d.next = head
        curr = d
        
        while curr and curr.next and curr.next.next:
            p1 = curr.next
            p2 = curr.next.next
            p1.next = p2.next
            p2.next = p1
            curr.next = p2
            curr = p1
            
        return d.next