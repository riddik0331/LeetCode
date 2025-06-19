# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root.left and not root.right:
            return [str(root.val)]
        res = []
        stack = [(root, str(root.val))]
        while stack:
            node, cur_path = stack.pop()
            if node.right:
                stack.append((node.right, cur_path + '->' + str(node.right.val)))
            if node.left:
                stack.append((node.left, cur_path + '->' + str(node.left.val)))
            if not node.left and not node.right:
                res.append(cur_path)

        return res
