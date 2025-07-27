class Solution:
    # def longestPalindrome(self, s: str) -> int:
    #     res = ''
    #     counter = Counter(s)
    #     flag_center = False
    #     for key in counter:
    #         while counter[key] > 1:
    #             counter[key] -= 2
    #             res = key + res + key
    #         if counter[key] == 1 and not flag_center:
    #             flag_center = True
    #             center = len(res) // 2
    #             res = res[:center] + key + res[center:]

    #     return len(res)


        def longestPalindrome(self, s: str) -> int:
            res = 0
            counter = Counter(s)
            flag_center = False
            for key in counter:
                while counter[key] > 1:
                    counter[key] -= 2
                    res += 2
                if counter[key] == 1 and not flag_center:
                    flag_center = True
                    res += 1

            return res
