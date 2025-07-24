class Solution:
    def toHex(self, num: int) -> str:
        res = ''
        hex_dict = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        if num < 0:
            num = 4294967296 + num
        while num >= 16:
            remainder = num % 16
            if remainder in range(10):
                res += str(remainder)
            else:
                res += hex_dict[remainder]
            num //= 16
        if num in range(10):
            res += str(num)
        else:
            res += hex_dict[num]

        return res[::-1]
