# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
        
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        if not root:
            return 0
        max_depth = 0
        queue = deque([(root, 1)])
        while queue:
            root, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            if root.left:
                queue.append((root.left, depth + 1))
            if root.right:
                queue.append((root.right, depth + 1))
        return max_depth
