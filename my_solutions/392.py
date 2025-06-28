class Solution:
    # def isSubsequence(self, s: str, t: str) -> bool:
    #     idx_s = 0
    #     idx_t = 0
    #     len_s = len(s)
    #     len_t = len(t)
    #     flag = False

    #     if len_s == 0:
    #         return True

    #     while idx_s < len_s:
    #         while idx_t < len_t:
    #             if s[idx_s] == t[idx_t]:
    #                 idx_t += 1
    #                 flag = True
    #                 break
    #             flag = False
    #             idx_t += 1
    #         if idx_s == len_s -1 and flag:
    #             return True
    #         elif idx_s == len_s - 1 and not flag:
    #             return False
    #         elif idx_t == len_t:
    #             return False
    #         idx_s += 1


    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if len(s) > len(t):
            return False
        s_idx = 0
        for t_idx in range(len(t)):
            if s[s_idx] == t[t_idx]:
                if s_idx == len(s) - 1:
                    return True
                s_idx += 1
        
        return False
