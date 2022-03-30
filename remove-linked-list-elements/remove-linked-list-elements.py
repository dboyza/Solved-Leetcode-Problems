# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        prev = ListNode(-1)
        
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
                if curr == head:
                    head = curr.next
            else:
                prev = curr
            curr = curr.next
            
        return head
            