# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def traverse(curr):
            print(curr.val)
            if curr == None:
                return 0
            if curr.left:
                traverse(curr.left)
            if curr.right:
                traverse(curr.right)
            if curr.val >= low and curr.val <= high:
                self.res += curr.val
        
        self.res = 0
        traverse(root)
        
        return self.res
                
            