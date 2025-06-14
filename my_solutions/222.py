# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def countNodes(self, root: Optional[TreeNode]) -> int:
    #     counter = 0
    #     if not root:
    #         return counter
    #     stack = [root]
    #     while stack:
    #         node = stack.pop()
    #         counter += 1
    #         if node.left:
    #             stack.append(node.left)
    #         if node.right:
    #             stack.append(node.right)
    #     return counter


    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
