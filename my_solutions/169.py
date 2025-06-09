class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        return max(counter, key=counter.get)
