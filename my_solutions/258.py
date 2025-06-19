class Solution:
    # def addDigits(self, num: int) -> int:
    #     if len(str(num)) == 1: #  Base case
    #         return num
    #     return self.addDigits(sum([int(i) for i in str(num)]))



    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            return 1 + (num-1) % 9
