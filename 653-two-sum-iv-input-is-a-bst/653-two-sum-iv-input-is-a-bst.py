# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # BFS Iterative
        return self.BFS(root, k)
    
    def BFS(self, curr, target):
            seen = {}
            queue = [curr]

            while len(queue) > 0:
                curr = queue.pop(0)
                if curr.val in seen:
                    return True
                else:
                    seen[target-curr.val] = True
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            return False
        
    
    