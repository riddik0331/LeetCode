class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        p_list = list(pattern)
        if len(p_list) != len(s_list):
            return False
        my_dict = {}
        for letter, word in zip(p_list, s_list):
            if  letter not in my_dict and word in my_dict.values():
                return False
            elif letter not in my_dict:
                my_dict[letter] = word
            elif my_dict[letter] != word:
                return False
        return True
