# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True
#         def treeLenth(node):
#             if not node:
#                 return 0
#             return 1 + max(treeLenth(node.left), treeLenth(node.right))
        
#         if abs(treeLenth(root.left) - treeLenth(root.right)) < 2:
#             return self.isBalanced(root.left) and self.isBalanced(root.right)
#         else:
#             return False        
        

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0  # высота пустого дерева = 0

            left = check(node.left)
            if left == -1:
                return -1  # левое поддерево не сбалансировано

            right = check(node.right)
            if right == -1:
                return -1  # правое поддерево не сбалансировано

            if abs(left - right) > 1:
                return -1  # текущий узел не сбалансирован

            return 1 + max(left, right)  # вернуть высоту поддерева

        return check(root) != -1
