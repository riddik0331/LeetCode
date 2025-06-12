class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Create dict for pairs of s/t symb
        symb_dict = {}
        # Run for each symb in s and t
        for i in range(len(s)):
            # Check if s-symb in dict and t-symb is correct for it
            if s[i] in symb_dict:
                if symb_dict[s[i]] != t[i]:
                    return False
            # Check if t-symb in dict, False if it is
            elif t[i] in symb_dict.values():
                return False
            # Add new pair of symb
            else:
                symb_dict[s[i]] = t[i]
        return True
