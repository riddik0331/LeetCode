class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        res = ''
        temp_num = columnNumber
        while temp_num:
            temp_num -= 1
            idx = temp_num % 26
            res = alph[idx] + res
            temp_num //= 26
        
        return res
