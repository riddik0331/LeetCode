class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        res = []
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        intersections = set(nums1) & set(nums2)
        for i in intersections:
            res.extend([i] * min(counter1[i], counter2[i]))
        
        return res
