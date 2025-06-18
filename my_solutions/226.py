# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if not root:
    #         return None
    #     self.invertTree(root.left)
    #     self.invertTree(root.right)
    #     root.left, root.right = root.right, root.left
    #     # swap(root.right, root.left)
    #     return root


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        from collections import deque
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root
