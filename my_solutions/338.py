class Solution:
    # def countBits(self, n: int) -> List[int]:
    #     res = []
    #     for i in range(n + 1):
    #         res.append(bin(i).count('1'))
    #     return res


    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res
