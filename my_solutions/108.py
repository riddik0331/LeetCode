# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]: # recursive method
    #     if not nums:
    #         return None
    #     mid = len(nums) // 2
    #     node_val = nums[mid]
    #     node_left = nums[:mid]
    #     node_right = nums[mid + 1:]
    #     node = TreeNode(
    #         val=node_val,
    #         left=self.sortedArrayToBST(node_left),
    #         right=self.sortedArrayToBST(node_right)
    #         )
    #     return node


    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:    #  Iterative method
        stack = [(0, len(nums) - 1, None, False)]
        while stack:
            start, end, parent, is_left = stack.pop()
            if start > end:
                continue
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            if parent:
                if is_left:
                    parent.left = node
                else:
                    parent.right = node
            else:
                root = node
            stack.append((mid + 1, end, node, False))
            stack.append((start, mid - 1, node, True))
        
        return root
