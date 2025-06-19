class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        from math import log
        if n <= 0:
            return False
        power = log(n, 2)
        pref = power - int(power)
        # return int(power) == power or 2**power - 2**int(power) < 0.9
        # return int(power), power, 2**power, 2**int(power)
        return power - int(power) < 0.0000000009


    # def isPowerOfTwo(self, n: int) -> bool:
    #     return n > 0 and (n & (n - 1)) == 0
