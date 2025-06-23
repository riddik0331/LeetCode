class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     from collections import Counter
    #     counter = Counter(nums)
    #     zero_count = counter[0]
    #     while 0 in nums:
    #          nums.remove(0)
    #     nums.extend([0] * zero_count)


    # def moveZeroes(self, nums: List[int]) -> None:
    #     from collections import Counter
    #     counter = Counter(nums)
    #     zero_count = counter[0]
    #     for i in range(zero_count):
    #         nums.remove(0)
    #     nums.extend([0] * zero_count)


    
    def moveZeroes(self, nums: List[int]) -> None:
        from collections import Counter
        counter = Counter(nums)
        zero_count = counter[0]
        nums[:] = list(filter(lambda x: x != 0, nums))
        nums.extend([0] * zero_count)
