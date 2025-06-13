class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        from collections import Counter
        counter = Counter(nums)
        # return list(counter.values())
        if any(val > 1 for val in counter.values()):
            return True
        else:
            return False
