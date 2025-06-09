class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        string = columnTitle[::-1]
        for i in range(len(string)):
            symb = string[i]
            res += (ord(symb) - 64) * (26 ** i)

        return res
