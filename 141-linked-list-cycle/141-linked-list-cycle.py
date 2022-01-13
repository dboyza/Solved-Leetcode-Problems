# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        slow = ListNode(-1)
        slow.next = head
        fast = head
        
        """
        If there is no cycle, the fast pointer will stop at the end of the linked list.
        If there is a cycle, the fast pointer will eventually meet with the slow pointer.
        """
        
        while fast:
            if fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
            
            