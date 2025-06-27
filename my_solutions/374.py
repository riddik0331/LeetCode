# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # if n == 1:
        #     return n
        start = 1
        end = n
        while start <= end:
            mid = (end + start) // 2
            my_guess = guess(mid)
            if not my_guess:
                return mid
            elif my_guess == -1:
                end = mid - 1
            else:
                start = mid + 1
        
        return mid
