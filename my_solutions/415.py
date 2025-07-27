class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        ten = 0
        lenth = max(len(num1), len(num2))
        num1 = list('0' * (lenth - len(num1)) + num1)
        num2 = list('0' * (lenth - len(num2)) + num2)
        g = 0
        while g < lenth:
            i, j = num1.pop(), num2.pop()
            sum_nums = str(int(i) + int(j) + ten)
            if len(sum_nums) > 1:
                ten = 1
                res += sum_nums[-1]
            else:
                ten = 0
                res += sum_nums
            g += 1
        if ten == 1:
            res += '1'
        return res[::-1]
