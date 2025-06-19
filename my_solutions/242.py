class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     from collections import Counter
    #     return Counter(s) == Counter(t)


    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))
