# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        before = None
        curr = head
        
        while curr:
            after = curr.next
            curr.next = before
            before = curr
            curr = after
        return before