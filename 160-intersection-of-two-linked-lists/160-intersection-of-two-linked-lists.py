# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        lenA = 0
        lenB = 0
        currA = headA
        currB = headB
        
        while currA:
            lenA += 1
            currA = currA.next
        
        while currB:
            lenB += 1
            currB = currB.next
        
        if lenA>lenB:
            for _ in range(lenA-lenB):
                headA = headA.next
        else:
            for _ in range(lenB-lenA):
                headB = headB.next
                
        while headA or headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            
        return None
        
            