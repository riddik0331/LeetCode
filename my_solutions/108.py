# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        med = len(nums) // 2
        node_val = nums[med]
        node_left = nums[:med]
        node_right = nums[med + 1:]
        node = TreeNode(
            val=node_val,
            left=self.sortedArrayToBST(node_left),
            right=self.sortedArrayToBST(node_right)
            )
        return node


