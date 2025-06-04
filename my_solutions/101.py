# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True
#         root_left = root.left
#         root_right = root.right
#         def checkSymetric(root1, root2):
#             if not root1 and not root2:
#                 return True
#             if (root1 and root1.val) != (root2 and root2.val):
#                 return False
#             return (
#                 checkSymetric(root1.left, root2.right)
#                 and
#                 checkSymetric(root1.right, root2.left)
#             )
#         return checkSymetric(root_left, root_right)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = []
        stack.append((root.left, root.right))

        while stack:
            left, right = stack.pop()

            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            stack.append((left.left, right.right))
            stack.append((left.right, right.left))

        return True

