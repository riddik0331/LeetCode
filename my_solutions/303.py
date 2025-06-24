# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums = nums

#     def sumRange(self, left: int, right: int) -> int:
#         return sum(self.nums[left:right + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


class NumArray:

    def __init__(self, nums: List[int]):
        self.sum_nums = nums[:]
        for i in range(1, len(nums)):
            self.sum_nums[i] += self.sum_nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.sum_nums[right] - (self.sum_nums[left - 1] if left else 0)
