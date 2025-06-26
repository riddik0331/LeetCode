class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # len_list = len(s)
        # s.reverse()
        s[:] = s[::-1]
