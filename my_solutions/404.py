# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0
        stack = [(root, False)]
        res = 0
        while stack:
            node, is_left = stack.pop()
            if node.left:
                stack.append((node.left, True))
            if node.right:
                stack.append((node.right, False))
            if not node.left and not node.right and is_left:
                res += node.val
        return res

        
