class Solution:
    def hammingWeight(self, n: int) -> int:
        n_str = format(n, '032b')
        res = n_str.count('1')  # Faster
        # res = sum(int(n) for n in n_str)  # Slower
        return res
