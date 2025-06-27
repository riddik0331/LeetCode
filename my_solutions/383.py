class Solution:
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     ransome_list = list(ransomNote)
    #     magazine_list = list(magazine)
    #     while ransome_list:
    #         cur_letter = ransome_list.pop()
    #         if cur_letter in magazine_list:
    #             cur_letter_idx = magazine_list.index(cur_letter)
    #             magazine_list[cur_letter_idx] = 0
    #         else:
    #             return False
    #     return True


    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_mag = Counter(magazine)
        for letter in ransomNote:
            if letter not in counter_mag:
                return False
            else:
                if counter_mag[letter] == 0:
                    return False
                else:
                    counter_mag[letter] -= 1
        return True
