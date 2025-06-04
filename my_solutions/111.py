# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def minDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     if not root.left and not root.right:
    #         return 1
        
    #     left_len = self.minDepth(root.left) if root.left else float('inf')
    #     right_len = self.minDepth(root.right) if root.right else float('inf')
    #     return 1 + min(left_len, right_len)


    def minDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        if not root:
            return 0
        
        queue = deque()
        queue.append((root, 1))  # к каждому узлу прикрепим его глубину
        
        while queue:
            node, depth = queue.popleft()
            
            # как только нашли лист — возвращаем глубину!
            if not node.left and not node.right:
                return depth
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
