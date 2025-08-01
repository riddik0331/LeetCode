class Solution:
    # def countSegments(self, s: str) -> int:
    #     res = []
    #     word = ''
    #     for i in s:
    #         if i != ' ':
    #             word += i
    #         elif i == ' ' and word:
    #             res.append(word)
    #             word = ''
    #     if word:
    #         res.append(word)

        # return len(res)


        def countSegments(self, s: str) -> int:
            res = s.split()
            
            return len(res)
