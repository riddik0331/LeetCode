class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for symb in s.lower():
            if symb.isalnum():
                res += symb
        if res == res[::-1]:
            return True
        else:
            return False
