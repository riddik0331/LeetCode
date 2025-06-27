class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx_s = 0
        idx_t = 0
        len_s = len(s)
        len_t = len(t)
        flag = False

        if len_s == 0:
            return True

        while idx_s < len_s:
            while idx_t < len_t:
                if s[idx_s] == t[idx_t]:
                    idx_t += 1
                    flag = True
                    break
                flag = False
                idx_t += 1
            if idx_s == len_s -1 and flag:
                return True
            elif idx_s == len_s - 1 and not flag:
                return False
            elif idx_t == len_t:
                return False
            idx_s += 1
            
