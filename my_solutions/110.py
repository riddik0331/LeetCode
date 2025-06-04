# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def treeLenth(node):
            if not node:
                return 1
            return 1 + max(treeLenth(node.left), treeLenth(node.right))
        
        if abs(treeLenth(root.left) - treeLenth(root.right)) < 2:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False        
        
