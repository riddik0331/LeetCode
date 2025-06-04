# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        from collections import deque
        if not root:
            return False
        queue = deque([(root, root.val)])
        while queue:
            node, sum_val = queue.popleft()
            if node.left:
                queue.append((node.left, sum_val + node.left.val))
            if node.right:
                queue.append((node.right, sum_val + node.right.val))
            if not node.left and not node.right and sum_val == targetSum:
                return True
        return False                
