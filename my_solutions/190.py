class Solution:
    # def reverseBits(self, n: int) -> int:
    #     n_ = format(n, '032b')
    #     rev_n = n_[::-1]
    #     dec = int(rev_n, 2)
    #     return dec


    # def reverseBits(self, n: int) -> int:
    #     res = 0
    #     for _ in range(32):
    #         res = res << 1 | n & 1
    #         n >>= 1
    #     return res


    def reverseBits(self, n: int) -> int:
        rev = 0
        for digit in range(32):
            rev |= (1 & (n >> digit)) << (31 - digit)
        return rev
