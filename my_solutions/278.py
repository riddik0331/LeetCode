# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # def firstBadVersion(self, n: int) -> int:
    #     k = n // 2 + n % 2
    #     n = n // 2 + n % 2
    #     if n == 0:
    #         return 1
    #     isbad_dict = {}
    #     while True:
    #         isbad_dict[n] = isBadVersion(n)
    #         if isbad_dict[n] and isbad_dict.get(n - 1, True):
    #             k = k // 2 + k % 2
    #             n -= k
    #         elif isbad_dict[n] and not isbad_dict.get(n - 1, True):
    #             return n
    #         else:
    #             k = k // 2 + k % 2
    #             n += k



    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while True:
            mid = (end + start) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
            if start >= end:
                return start
