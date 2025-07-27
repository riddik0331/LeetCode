class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums), reverse=True)
        if len(sorted_nums) > 2:
            return sorted_nums[2]
        else:
            return sorted_nums[0]
