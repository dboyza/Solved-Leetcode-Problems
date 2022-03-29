# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        check = []
        curr = head
        
        while curr:
            check.append(curr.val)
            curr = curr.next
        
        return check == check[::-1]